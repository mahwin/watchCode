# 조사 원본 데이터 (2026년 10월 수집)

| 파일 | 내용 |
|---|---|
| `reference_uma/videos.json` | 레퍼런스 채널 「ウマい健康雑学」 영상 29개 (제목, 조회수, 길이, 썸네일 주소) |
| `reference_uma/video_<ID>.json` | 상위 3개 영상(커피 7LSymhoLns8, 보리차 1Q2fRTBqn4Y, 지방간 mwR5zTaWSpU)의 설명란, '가장 많이 다시 본 구간'(100구간), 댓글 60개 |
| `kr_food_demand_raw.json` | 한국 YouTube "매일 ○○ 먹으면" 28개 음식 검색 결과 (조회수순 상위 15개) |
| `shorts_demand_raw.json` | 한국 건강·노후 숏츠 검색 결과 (2026-10-19, 14개 검색어, 조회수·채널) |
| `format_demand_raw.json` | 새 형식 수요 측정 (2026-10-19): 신호형·제도형·퀴즈형 등 22개 검색어 결과 |

새로 수집할 때는 `tools/yt.py`, `tools/demand_scan.py`를 씁니다.
