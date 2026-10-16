"""오래 박사 그림의 색을 사람 캐릭터에 맞추는 채도 보정 (2026-10-16 B안).

채도 x0.72, 빨강(넥타이)은 x0.9로 거의 유지, 남색은 밝기 x1.18. 거의 흰색인 픽셀은 건드리지 않습니다.
새로 만든 오래 박사 그림이 사람 캐릭터보다 쨍할 때 씁니다. 사람이 함께 있는 장면에는 쓰지 않습니다.

사용법:
    python3 tools/color_match.py 입력.png [출력.png] [--keep 255,242,212]
    (출력을 생략하면 입력 이름 뒤에 _matched를 붙여 저장, --keep은 보존할 배경색)
"""
import colorsys
import os
import sys

from PIL import Image


def grade(rgb, s_scale=0.72, v_scale_blue=1.18):
    r, g, b = rgb
    if r > 240 and g > 240 and b > 240:
        return rgb
    h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
    hd = h * 360
    k = s_scale
    if (hd < 15 or hd > 345) and s > 0.5:
        k = max(s_scale, 0.9)
    s = min(1, s * k)
    if 195 <= hd <= 240 and s > 0.2:
        v = min(1, v * v_scale_blue)
    r2, g2, b2 = colorsys.hsv_to_rgb(h, s, v)
    return (int(r2 * 255), int(g2 * 255), int(b2 * 255))


def match_image(path, keep=None):
    im = Image.open(path).convert('RGB')
    px = im.load()
    cache = {}
    for y in range(im.height):
        for x in range(im.width):
            c = px[x, y]
            if keep and sum(abs(a - b) for a, b in zip(c, keep)) <= 12:
                continue
            n = cache.get(c)
            if n is None:
                n = cache[c] = grade(c)
            px[x, y] = n
    return im


if __name__ == '__main__':
    args = sys.argv[1:]
    keep = None
    if '--keep' in args:
        i = args.index('--keep')
        keep = tuple(int(v) for v in args[i + 1].split(','))
        del args[i:i + 2]
    if not args:
        print(__doc__)
        sys.exit(1)
    src = args[0]
    dst = args[1] if len(args) > 1 else '%s_matched%s' % os.path.splitext(src)
    match_image(src, keep).save(dst, optimize=True)
    print('저장:', dst)
