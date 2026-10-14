# shortsDrama: 시니어 반전 숏드라마 제작 키트

레퍼런스 채널 「훈작가의 숏드라마」(쇼츠 238개, 누적 2억 회)를 분석해서 만든 쇼츠 제작 프롬프트 모음이에요.

## 구성
```
shortsDrama/
├── CLAUDE.md                 # Claude Code 작업 지침 (파이프라인)
├── analysis.md               # 잘된 영상 vs 안된 영상 상세 비교
├── prompts/
│   ├── 01_topic.md           # 주제·제목 기획 (점수화)
│   ├── 02_script.md          # 2분 대사 대본 (6구간 구조와 자가 점검)
│   ├── 03_characters.md      # 캐릭터 고정 시트
│   ├── 04_shotlist.md        # 컷 분할과 컷별 이미지·영상 프롬프트 (MODE A/B)
│   ├── 05_thumbnail_upload.md# 썸네일·제목·해시태그·업로드 체크리스트
│   └── 06_qc_edit.md         # 검수·편집·렌더링 가이드
├── bgm.md                    # 무료 배경음악 출처와 추천곡
├── examples/ep001_taxi.md    # 완성 예시 1편
└── episodes/                 # 생성되는 에피소드 저장 위치
```

## 사용법 (Claude Code)
```bash
cd shortsDrama
claude
> 주제 후보 20개 뽑아줘
> backlog 상위 1개로 에피소드 만들어줘, MODE B
```

## 제작 흐름
주제·제목 → 대사 대본 → 캐릭터 고정 → 컷 분할과 프롬프트 → 컷별 이미지 → (영상 생성 또는 TTS) → 검수 → 자막·효과음 편집 → 렌더링 → 썸네일·업로드
