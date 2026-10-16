"""캐릭터 시트를 한 장씩 잘라 배경을 투명하게 만든 PNG로 저장합니다.

    python3 tools/cutout.py [출력폴더]      # 기본: assets/characters/cutouts

시트를 고해상도 버전으로 바꿔도 배치(줄 수, 줄마다 개수)가 같으면 그대로 다시 실행하면 됩니다.
배치가 바뀌면 아래 SHEETS의 이름 목록을 고칩니다.
"""
import os
import sys
from collections import deque

from PIL import Image

KIT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHAR = os.path.join(KIT, 'assets', 'characters')

# (시트 파일, 저장 폴더, 큰 전신 이름 또는 None, 줄별 이름 목록)
# 이름은 '파일명|한글 설명'
SHEETS = [
    ('orae_master.png', 'deer', None, [['deer_00_basic|오래 박사 기본 전신']]),
    ('orae_expressions.png', 'deer', None, [[
        'deer_face_01_smile|미소', 'deer_face_02_surprised|놀람', 'deer_face_03_warning|검지 경고',
        'deer_face_04_thinking|턱 괴고 생각', 'deer_face_05_wink|윙크 엄지척']]),
    ('orae_poses.png', 'deer', None, [
        ['deer_pose_01_board|화이트보드 설명', 'deer_pose_02_report|자료 보며 생각', 'deer_pose_03_point|놀라며 가리킴'],
        ['deer_pose_04_money|동전·태블릿 (경제)', 'deer_pose_05_bow|가슴에 손 인사', 'deer_pose_06_thumbsup|엄지척']]),
    ('man_sheet.png', 'man', 'man_00_basic|남성 기본 전신', [
        ['man_turn_1_front|정면', 'man_turn_2_three_quarter|3/4 측면', 'man_turn_3_side|옆모습', 'man_turn_4_back|뒷모습'],
        ['man_face_01_smile|미소', 'man_face_02_yummy|맛있음', 'man_face_03_surprised|놀람',
         'man_face_04_worried|걱정', 'man_face_05_tired|피곤', 'man_face_06_laugh|활짝 웃음'],
        ['man_act_01_drink|컵으로 마시기', 'man_act_02_eat|밥 먹기', 'man_act_03_stomachache|배 아픔',
         'man_act_04_backpain|허리 통증', 'man_act_05_passbook|통장 보며 걱정', 'man_act_06_thumbsup|엄지척']]),
    ('woman_sheet.png', 'woman', 'woman_00_basic|여성 기본 전신', [
        ['woman_turn_1_front|정면', 'woman_turn_2_three_quarter|3/4 측면', 'woman_turn_3_side|옆모습', 'woman_turn_4_back|뒷모습'],
        ['woman_face_01_smile|미소', 'woman_face_02_yummy|맛있음', 'woman_face_03_surprised|놀람',
         'woman_face_04_worried|걱정', 'woman_face_05_tired|피곤', 'woman_face_06_laugh|활짝 웃음'],
        ['woman_act_01_drink|컵으로 마시기', 'woman_act_02_eat|밥 먹기', 'woman_act_03_stomachache|배 아픔',
         'woman_act_04_mirror|거울 보기 (피부)', 'woman_act_05_hotflash|열감 (갱년기)', 'woman_act_06_phone|휴대폰 보기']]),
]

INK = 232      # 이보다 어두운 채널이 있으면 그림으로 봄
SCALE = 4      # 위치 찾기용 축소 배율


def find_pieces(im):
    """축소 이미지에서 덩어리를 찾고, 작은 조각(물음표, 효과선)은 가장 가까운 큰 덩어리에 붙인다."""
    w, h = im.width // SCALE, im.height // SCALE
    px = im.resize((w, h), Image.BOX).load()
    ink = [[min(px[x, y]) < INK for x in range(w)] for y in range(h)]
    seen = [[False] * w for _ in range(h)]
    comps = []
    for y in range(h):
        for x in range(w):
            if not ink[y][x] or seen[y][x]:
                continue
            q = deque([(x, y)])
            seen[y][x] = True
            x0 = x1 = x
            y0 = y1 = y
            n = 0
            while q:
                cx, cy = q.popleft()
                n += 1
                x0, x1, y0, y1 = min(x0, cx), max(x1, cx), min(y0, cy), max(y1, cy)
                for nx, ny in ((cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1)):
                    if 0 <= nx < w and 0 <= ny < h and ink[ny][nx] and not seen[ny][nx]:
                        seen[ny][nx] = True
                        q.append((nx, ny))
            comps.append((n, [x0 * SCALE, y0 * SCALE, (x1 + 1) * SCALE, (y1 + 1) * SCALE]))
    biggest = max(n for n, _ in comps)
    big = [b for n, b in comps if n >= biggest * 0.15]
    for n, b in comps:
        if n >= biggest * 0.15 or n < 3:
            continue
        cx, cy = (b[0] + b[2]) / 2, (b[1] + b[3]) / 2

        def dist(B):
            dx = max(B[0] - cx, 0, cx - B[2])
            dy = max(B[1] - cy, 0, cy - B[3])
            return dx * dx + dy * dy
        t = min(big, key=dist)
        t[0], t[1], t[2], t[3] = min(t[0], b[0]), min(t[1], b[1]), max(t[2], b[2]), max(t[3], b[3])
    return [{'box': b, 'clip': None} for b in big]


def seam_split(im, piece):
    """맞붙은 두 그림 사이를 잉크가 가장 적은 세로선으로 가른다."""
    x0, y0, x1, y1 = piece['box']
    lo, hi = x0 + int((x1 - x0) * 0.35), x0 + int((x1 - x0) * 0.65)
    px = im.load()
    cols = range(lo, hi)
    cost = [[255 - min(px[x, y]) for x in cols] for y in range(y0, y1)]
    acc = [cost[0][:]]
    for r in range(1, len(cost)):
        prev = acc[-1]
        acc.append([cost[r][i] + min(prev[max(i - 1, 0):i + 2]) for i in range(len(cols))])
    i = min(range(len(cols)), key=lambda k: acc[-1][k])
    seam = [0] * len(cost)
    for r in range(len(cost) - 1, -1, -1):
        seam[r] = lo + i
        if r:
            cand = range(max(i - 1, 0), min(i + 2, len(cols)))
            i = min(cand, key=lambda k: acc[r - 1][k])
    seam = {y0 + r: x for r, x in enumerate(seam)}
    left = {'box': [x0, y0, max(seam.values()) + 1, y1], 'clip': ('keep_left', seam)}
    right = {'box': [min(seam.values()), y0, x1, y1], 'clip': ('keep_right', seam)}
    return left, right


def arrange(im, pieces, master, rows):
    out = []
    if master:
        m = max(pieces, key=lambda p: p['box'][3] - p['box'][1])
        pieces.remove(m)
        out.append((master, m))
    pieces.sort(key=lambda p: (p['box'][1] + p['box'][3]) / 2)
    hs = sorted(p['box'][3] - p['box'][1] for p in pieces)
    gap = hs[len(hs) // 2] * 0.5
    groups = []
    for p in pieces:
        c = (p['box'][1] + p['box'][3]) / 2
        if groups and abs(c - groups[-1][0]) < gap:
            groups[-1][1].append(p)
        else:
            groups.append([c, [p]])
    if len(groups) != len(rows):
        raise SystemExit('줄 수가 다릅니다: 찾은 %d줄, 예상 %d줄' % (len(groups), len(rows)))
    for (_, row), names in zip(groups, rows):
        while len(row) < len(names):
            widest = max(row, key=lambda p: p['box'][2] - p['box'][0])
            row.remove(widest)
            row.extend(seam_split(im, widest))
        if len(row) != len(names):
            raise SystemExit('한 줄의 개수가 다릅니다: 찾은 %d개, 예상 %d개' % (len(row), len(names)))
        row.sort(key=lambda p: p['box'][0])
        out.extend(zip(names, row))
    return out


def render(im, piece, pad=8):
    x0, y0, x1, y1 = piece['box']
    x0, y0 = max(x0 - pad, 0), max(y0 - pad, 0)
    x1, y1 = min(x1 + pad, im.width), min(y1 + pad, im.height)
    crop = im.crop((x0, y0, x1, y1))
    w, h = crop.size
    px = crop.load()
    bg = [[False] * w for _ in range(h)]
    q = deque()
    if piece['clip']:
        side, seam = piece['clip']
        for y in range(h):
            s = seam.get(y + y0)
            if s is None:
                continue
            for x in range(w):
                if (side == 'keep_left' and x + x0 > s) or (side == 'keep_right' and x + x0 < s):
                    bg[y][x] = True
    for y in range(h):
        for x in range(w):
            if bg[y][x] or ((x in (0, w - 1) or y in (0, h - 1)) and min(px[x, y]) > INK):
                bg[y][x] = True
                q.append((x, y))
    while q:
        cx, cy = q.popleft()
        for nx, ny in ((cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1)):
            if 0 <= nx < w and 0 <= ny < h and not bg[ny][nx] and min(px[nx, ny]) > INK:
                bg[ny][nx] = True
                q.append((nx, ny))
    # 자를 범위 가장자리에 닿은 그림은 옆 캐릭터의 조각이므로 지운다
    for y in range(h):
        for x in range(w):
            if (x in (0, w - 1) or y in (0, h - 1)) and not bg[y][x]:
                bg[y][x] = True
                q.append((x, y))
    while q:
        cx, cy = q.popleft()
        for nx, ny in ((cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1)):
            if 0 <= nx < w and 0 <= ny < h and not bg[ny][nx]:
                bg[ny][nx] = True
                q.append((nx, ny))
    out = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    op = out.load()
    for y in range(h):
        for x in range(w):
            if bg[y][x]:
                continue
            r, g, b = px[x, y]
            edge = any(0 <= x + dx < w and 0 <= y + dy < h and bg[y + dy][x + dx]
                       for dx in (-2, -1, 0, 1, 2) for dy in (-2, -1, 0, 1, 2))
            if edge:
                # 흰 배경과 섞인 가장자리 픽셀을 반투명 외곽선 색으로 되돌림
                a = min(1.0, (255 - min(r, g, b)) / 185)
                if a <= 0.02:
                    continue
                r, g, b = (max(0, min(255, int((c - (1 - a) * 255) / a))) for c in (r, g, b))
                op[x, y] = (r, g, b, int(a * 255))
            else:
                op[x, y] = (r, g, b, 255)
    bbox = out.getbbox()
    if bbox:
        bx0, by0, bx1, by1 = bbox
        out = out.crop((max(bx0 - pad, 0), max(by0 - pad, 0), min(bx1 + pad, w), min(by1 + pad, h)))
    return out


def main(dst):
    listing = []
    for sheet, folder, master, rows in SHEETS:
        im = Image.open(os.path.join(CHAR, sheet)).convert('RGB')
        os.makedirs(os.path.join(dst, folder), exist_ok=True)
        for name, piece in arrange(im, find_pieces(im), master, rows):
            fname, label = name.split('|')
            out = render(im, piece)
            path = os.path.join(dst, folder, fname + '.png')
            out.save(path, optimize=True)
            listing.append((folder, fname + '.png', label, out.size))
            print('%-6s %-34s %4dx%-4d %s' % (folder, fname + '.png', out.size[0], out.size[1], label))
    return listing


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else os.path.join(CHAR, 'cutouts'))
