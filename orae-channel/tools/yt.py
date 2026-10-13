"""YouTube 공개 데이터 수집 도구 (표준 라이브러리만 사용).

클라우드 환경에서도 동작하는 범위만 다룹니다. 영상 파일과 자막은 봇 확인으로 막혀 있어 수집하지 않습니다.

사용법:
  python3 tools/yt.py channels "건강 정보"            # 채널 검색 (구독자 수 포함)
  python3 tools/yt.py videos "매일 계란 먹으면"        # 조회수순 영상 검색
  python3 tools/yt.py channel @handle                  # 채널 최신 영상 + 인기 영상
  python3 tools/yt.py video VIDEO_ID                   # 설명란, 가장 많이 다시 본 구간, 댓글 (JSON 저장)
  python3 tools/yt.py thumbs @handle out.jpg           # 최신 영상 썸네일 모음 이미지 (Pillow 필요)
"""
import json
import re
import sys
import time
import urllib.parse
import urllib.request

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"
CLIENT = {"clientName": "WEB", "clientVersion": "2.20250101.00.00", "hl": "ko", "gl": "KR"}


def _get(url, data=None, lang="ko-KR"):
    headers = {"User-Agent": UA, "Accept-Language": lang}
    if data is not None:
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=data, headers=headers)
    return urllib.request.urlopen(req, timeout=30).read()


def _initial_data(html):
    m = re.search(r"var ytInitialData = (\{.*?\});</script>", html)
    if not m:
        raise RuntimeError("ytInitialData를 찾지 못했습니다 (차단 또는 페이지 구조 변경)")
    return json.loads(m.group(1))


def _api(endpoint, body):
    body = dict(body, context={"client": CLIENT})
    return json.loads(_get(f"https://www.youtube.com/youtubei/v1/{endpoint}", json.dumps(body).encode()))


def walk(obj, key):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == key:
                yield v
            yield from walk(v, key)
    elif isinstance(obj, list):
        for item in obj:
            yield from walk(item, key)


def _text(node):
    if not node:
        return ""
    if "simpleText" in node:
        return node["simpleText"]
    return "".join(r.get("text", "") for r in node.get("runs", []))


def parse_count(text):
    """'조회수 1,234회', '43만', '1.2천' 같은 표기를 정수로 바꿉니다."""
    t = (text or "").replace(",", "")
    m = re.search(r"([0-9.]+)\s*(만|천|억|K|M)?", t)
    if not m:
        return 0
    n = float(m.group(1))
    unit = {"천": 1e3, "만": 1e4, "억": 1e8, "K": 1e3, "M": 1e6}.get(m.group(2), 1)
    return int(n * unit)


def search_channels(query):
    url = "https://www.youtube.com/results?search_query=" + urllib.parse.quote(query) + "&sp=EgIQAg%253D%253D"
    data = _initial_data(_get(url).decode("utf-8", "ignore"))
    out = []
    for c in walk(data, "channelRenderer"):
        # 핸들이 있는 채널은 videoCountText 자리에 구독자 수가 들어옵니다.
        subs = _text(c.get("videoCountText")) or _text(c.get("subscriberCountText"))
        out.append({"title": _text(c.get("title")), "handle": _text(c.get("subscriberCountText")),
                    "subscribers": subs, "channel_id": c.get("channelId")})
    return out


def search_videos(query, sort_by_views=True):
    sp = "CAMSAhAB" if sort_by_views else "EgIQAQ%253D%253D"
    url = "https://www.youtube.com/results?search_query=" + urllib.parse.quote(query) + "&sp=" + sp
    data = _initial_data(_get(url).decode("utf-8", "ignore"))
    out = []
    for v in walk(data, "videoRenderer"):
        views_text = _text(v.get("viewCountText"))
        out.append({"title": _text(v.get("title")), "channel": _text(v.get("ownerText")),
                    "views": parse_count(views_text), "views_text": views_text,
                    "published": _text(v.get("publishedTimeText")), "length": _text(v.get("lengthText")),
                    "video_id": v.get("videoId")})
    return out


def _lockups(data, limit):
    out = []
    for lv in walk(data, "lockupViewModel"):
        md = lv.get("metadata", {}).get("lockupMetadataViewModel", {})
        parts = [p.get("text", {}).get("content", "") for rows in walk(md, "metadataRows")
                 for row in rows for p in row.get("metadataParts", [])]
        sources = next(walk(lv, "sources"), [])
        out.append({"title": md.get("title", {}).get("content", ""), "meta": " · ".join(parts),
                    "length": next((b.get("text") for b in walk(lv, "thumbnailBadgeViewModel")), ""),
                    "thumbnail": sources[-1]["url"] if sources else "", "video_id": lv.get("contentId")})
        if len(out) >= limit:
            break
    return out


def channel_videos(handle_or_id, limit=30):
    """채널의 최신 영상과 인기 영상 목록을 돌려줍니다."""
    path = f"channel/{handle_or_id}" if handle_or_id.startswith("UC") else handle_or_id
    if path.startswith("@"):
        path = "@" + urllib.parse.quote(path[1:])
    data = _initial_data(_get(f"https://www.youtube.com/{path}/videos").decode("utf-8", "ignore"))
    latest = _lockups(data, limit)
    popular = []
    for chip in walk(data, "chipViewModel"):
        if chip.get("text") in ("인기순", "Popular"):
            token = next(walk(chip, "token"), None)
            if token:
                popular = _lockups(_api("browse", {"continuation": token}), limit)
    meta = next(walk(data, "channelMetadataRenderer"), {})
    return {"title": meta.get("title"), "description": meta.get("description"),
            "channel_id": meta.get("externalId"), "latest": latest, "popular": popular}


def video_details(video_id, comment_pages=3):
    """설명란, '가장 많이 다시 본 구간' 그래프, 댓글(내용·공감 수)을 돌려줍니다."""
    nxt = _api("next", {"videoId": video_id})
    desc = next(walk(nxt, "attributedDescription"), {}).get("content", "")
    heat = next((m for m in walk(nxt, "markers")
                 if isinstance(m, list) and m and "intensityScoreNormalized" in m[0]), [])
    token = None
    for section in walk(nxt, "itemSectionRenderer"):
        if section.get("sectionIdentifier") == "comment-item-section":
            token = next(walk(section, "token"), None)
    comments = []
    for _ in range(comment_pages):
        if not token:
            break
        page = _api("next", {"continuation": token})
        for e in walk(page, "commentEntityPayload"):
            props, bar = e.get("properties", {}), e.get("toolbar", {})
            comments.append({"text": props.get("content", {}).get("content", ""),
                             "likes": bar.get("likeCountNotliked") or bar.get("likeCountLiked"),
                             "published": props.get("publishedTime")})
        token = None
        for item in walk(page, "continuationItemRenderer"):
            token = next(walk(item, "token"), None)
        time.sleep(1)
    peaks = sorted(heat, key=lambda m: -m["intensityScoreNormalized"])[:8]
    peak_times = [f'{int(m["startMillis"]) // 60000}:{int(m["startMillis"]) // 1000 % 60:02d}' for m in
                  sorted(peaks, key=lambda m: int(m["startMillis"]))]
    return {"video_id": video_id, "description": desc, "replay_peaks": peak_times, "heatmap": heat,
            "comments": comments}


def thumbnail_sheet(items, out_path, cols=4):
    from io import BytesIO
    from PIL import Image, ImageDraw
    w, h = 480, 270
    rows = (len(items) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * w, rows * (h + 24)), "white")
    draw = ImageDraw.Draw(sheet)
    for i, it in enumerate(items):
        try:
            img = Image.open(BytesIO(_get(it["thumbnail"]))).convert("RGB").resize((w, h))
        except Exception:
            img = Image.new("RGB", (w, h), "gray")
        x, y = (i % cols) * w, (i // cols) * (h + 24)
        sheet.paste(img, (x, y))
        draw.text((x + 4, y + h + 4), f"#{i + 1} {it.get('meta', '')[:60]}", fill="black")
    sheet.save(out_path, quality=85)


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return
    cmd, arg = argv[1], argv[2]
    if cmd == "channels":
        for c in search_channels(arg)[:10]:
            print(f'{c["title"]} | {c["handle"]} | {c["subscribers"]} | {c["channel_id"]}')
    elif cmd == "videos":
        for v in search_videos(arg)[:15]:
            print(f'{v["views"]:>11,} | {v["published"]:<8} | {v["length"]:>7} | {v["channel"][:16]:<16} | {v["title"][:70]}')
    elif cmd == "channel":
        d = channel_videos(arg)
        print("##", d["title"], d["channel_id"])
        for label in ("latest", "popular"):
            print(f"-- {label}")
            for v in d[label][:12]:
                print(f'   [{v["length"]:>7}] {v["meta"][:28]:<28} {v["title"][:80]}')
    elif cmd == "video":
        d = video_details(arg)
        out = f"video_{arg}.json"
        json.dump(d, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print("설명란 앞부분:\n", d["description"][:800])
        print("\n가장 많이 다시 본 구간:", d["replay_peaks"])
        print(f"댓글 {len(d['comments'])}개 → {out} 저장")
    elif cmd == "thumbs":
        d = channel_videos(arg)
        out = argv[3] if len(argv) > 3 else "thumbs.jpg"
        thumbnail_sheet(d["latest"][:12], out)
        print("저장:", out)
    else:
        print(__doc__)


if __name__ == "__main__":
    main(sys.argv)
