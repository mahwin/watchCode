"""주제(음식 등) 수요 측정: "매일 ○○ 먹으면"을 조회수순으로 검색해 건강 정보 영상의 조회수를 셉니다.

사용법:
  python3 tools/demand_scan.py 계란 두부 토마토
  python3 tools/demand_scan.py --verb 마시면 커피 보리차
  python3 tools/demand_scan.py --query "{}을 매일 먹으면" 고구마      # 검색어 틀 직접 지정 ({} 자리에 주제)

결과: 표를 출력하고 demand_<날짜>.json으로 저장합니다.
판단 기준(03_포맷공식): 100만 회 넘은 건강 영상이 있으면 수요가 검증된 것으로 봅니다.
"""
import datetime
import json
import os
import re
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yt import search_videos  # noqa: E402

HEALTH = re.compile(r"효능|건강|혈당|혈관|당뇨|염증|일어나는|생기는|몸|간 |간이|간에|암|치매|뱃살|부작용|이유|안되는|안 되는|"
                    r"주의|변화|콜레스테롤|혈압|장 |장건강|노화|수명|의사|약사|한의|박사|교수|원장|독|최악|상극|절대|연금|세금|노후")


def scan(topic, query_tpl):
    q = query_tpl.format(topic)
    videos = search_videos(q)[:15]
    rel = sorted([v for v in videos if topic in v["title"] and HEALTH.search(v["title"])], key=lambda v: -v["views"])
    return {"topic": topic, "query": q,
            "max_views": rel[0]["views"] if rel else 0,
            "over_1m": sum(v["views"] >= 1_000_000 for v in rel),
            "over_300k": sum(v["views"] >= 300_000 for v in rel),
            "top": rel[:5]}


def main(argv):
    args = argv[1:]
    verb, tpl = "먹으면", None
    if "--verb" in args:
        i = args.index("--verb"); verb = args[i + 1]; del args[i:i + 2]
    if "--query" in args:
        i = args.index("--query"); tpl = args[i + 1]; del args[i:i + 2]
    if not args:
        print(__doc__)
        return
    tpl = tpl or ("매일 {} " + verb)
    rows = []
    for topic in args:
        try:
            rows.append(scan(topic, tpl))
        except Exception as e:  # 일시 차단 등
            print(f"{topic}: 실패 ({e})")
        time.sleep(1.5)
    rows.sort(key=lambda r: (-r["over_1m"], -r["max_views"]))
    print(f'{"주제":<8} {"최고 조회수":>12} {"100만+":>6} {"30만+":>6}  최고 영상')
    for r in rows:
        top = r["top"][0] if r["top"] else {"channel": "", "title": ""}
        print(f'{r["topic"]:<8} {r["max_views"]:>12,} {r["over_1m"]:>6} {r["over_300k"]:>6}  {top["channel"][:12]} | {top["title"][:50]}')
    out = f"demand_{datetime.date.today():%Y%m%d}.json"
    json.dump(rows, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("저장:", out)


if __name__ == "__main__":
    main(sys.argv)
