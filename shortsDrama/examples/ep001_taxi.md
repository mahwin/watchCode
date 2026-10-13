# EP001 예시: 「택시에서 태어난 아이」

파이프라인 전체를 한 편에 적용한 예시예요. 새 에피소드는 이 형식을 따라 만들어요.

## 기획
- **제목:** 상견례에 작업복 입고 온 택시기사 아버지를 무시한 예비시어머니… 가방에서 떨어진 명찰 하나에 대반전
- **로그라인:** 의사 아들을 둔 부잣집 예비시어머니가 택시기사 사돈을 무시하고 파혼을 선언한다. 그때 그녀의 가방에서 30년간 간직한 낡은 명찰이 떨어지는데, 그건 그녀가 택시에서 아들을 낳던 밤에 아기를 받아 준 기사의 명찰이었다.
- **복선:** 25초에 민재가 "저 택시 안에서 태어났다면서요"라고 말하고, 덕수가 멈칫한다 → 75초에 명찰로 회수
- **점수:** 분노 5, 반전 5, 복선 5, 1초 이해도 4, 신선도 4 = 23/25

## 캐릭터 (identity_tag)
| id | 이름 | 역할 | identity_tag |
|---|---|---|---|
| C1 | 김덕수 | 피해자, 신부 아버지 | `Deoksu, 63-year-old Korean man, taxi driver, short gray crew cut, sun-tanned deeply wrinkled face, kind tired eyes, navy work jacket with a small faded name badge on chest` |
| C2 | 박영순 | 가해자, 예비시어머니 | `Yeongsun, 62-year-old wealthy Korean woman, voluminous permed dark brown hair, pearl necklace and pearl earrings, cream tweed jacket with silk scarf, sharp proud eyes` |
| C3 | 민재 | 신랑, 의사 | `Minjae, 30-year-old Korean man, neat short black hair, clean navy suit, gentle face` |
| C4 | 지은 | 신부 | `Jieun, 29-year-old Korean woman, long straight black hair, modest beige dress, soft kind face` |

**공통 장소 문구 (모든 컷에 동일):**
`upscale traditional Korean restaurant private room, wooden lattice doors, low table with white tablecloth and banchan dishes, warm soft lighting`

**목소리:** 덕수는 낮고 차분한 표준어. 영순은 높고 또박또박하며 비꼬는 톤. 민재는 부드러운 30대 남성. 지은은 맑은 20대 여성.

## 컷 리스트 (MODE A, 17컷, 약 120초)

> 아래 `[C1]`~`[C4]`는 위 identity_tag로, `[ROOM]`은 공통 장소 문구로 바꿔 넣으세요.
> 이미지 프롬프트 앞에는 항상 `Photorealistic Korean TV drama still, 9:16 vertical, cinematic, ultra realistic, 35mm,`를 붙이고, 뒤에는 `no text, no subtitles, no watermark`를 붙여요.

| # | 초 | 대사 | 이미지 프롬프트 | 영상 프롬프트 (MODE A) |
|---|---|---|---|---|
| 1 | 6 | 덕수: "늦어서 죄송합니다. 손님 모셔다드리고 오느라…" | [ROOM], medium shot, [C1] entering through the lattice door, wiping sweat from forehead, bowing apologetically | [Camera] static [Action] he bows twice while stepping in [Dialogue] the old man says in Korean, apologetic and out of breath: "늦어서 죄송합니다. 손님 모셔다드리고 오느라…" [Audio] quiet restaurant ambience |
| 2 | 6 | 영순: "상견례에… 작업복을 입고 오셨네요?" | [ROOM], close-up of [C2] seated, looking him up and down with a contemptuous smirk | [Camera] slow push-in [Action] her eyes scan down and up [Dialogue] the woman in pearls says in Korean, mocking and slow: "상견례에… 작업복을 입고 오셨네요?" |
| 3 | 5 | 덕수: "아, 갈아입을 시간이 없어서요. 죄송합니다." | [ROOM], close-up of [C1], embarrassed smile, hand rubbing the back of his head | [Camera] static [Dialogue] the old man says in Korean, embarrassed: "아, 갈아입을 시간이 없어서요. 죄송합니다." |
| 4 | 7 | 지은: "아빠는 30년째 개인택시 하세요." / 영순: "택시요?" | [ROOM], medium two-shot, [C4] speaking proudly beside [C1], [C2] across the table | [Camera] static [Dialogue] the young woman says in Korean, proudly: "아빠는 30년째 개인택시 하세요." then the woman in pearls laughs and says: "택시요?" |
| 5 | 7 | 영순: "민재야, 너 이런 얘기는 안 했잖니." / 민재: "엄마, 그게 무슨 상관이에요." | [ROOM], over-the-shoulder shot, [C2] turning to [C3], [C3] frowning | [Camera] static [Dialogue] the woman says in Korean, displeased: "민재야, 너 이런 얘기는 안 했잖니." then the young man says firmly: "엄마, 그게 무슨 상관이에요." |
| 6 | 6 | 영순: "우리 집은 대대로 의사 집안이에요." | [ROOM], close-up of [C2] with chin raised, arrogant, touching her pearl necklace | [Camera] slow push-in [Dialogue] the woman says in Korean, arrogant: "상관이 왜 없어. 우리 집은 대대로 의사 집안이에요." |
| 7 ⭐복선 | 8 | 민재: "엄마도 옛날엔 힘들게 사셨잖아요. 저 택시 안에서 태어났다면서요." / 영순: "쓸데없는 소리를!" | [ROOM], medium shot, [C3] speaking casually, [C2] flustered in background | [Camera] static [Dialogue] the young man says in Korean, casually: "엄마도 옛날엔 힘들게 사셨잖아요. 저 택시 안에서 태어났다면서요." then the woman snaps: "쓸데없는 소리를!" |
| 8 ⭐복선 | 4 | (대사 없음) 덕수 멈칫 | [ROOM], extreme close-up of [C1]'s eyes, subtle realization, frozen | [Camera] very slow push-in [Action] his eyes widen slightly, he glances at the woman [Audio] room tone only |
| 9 | 8 | 영순: "솔직히 말씀드릴게요. 우리 민재가 아까워요. 집안 수준은 맞아야죠." | [ROOM], close-up of [C2] leaning forward, cold expression | [Camera] static [Dialogue] the woman says in Korean, cold and deliberate: "솔직히 말씀드릴게요. 우리 민재가 아까워요. 집안 수준은 맞아야죠." |
| 10 | 7 | 덕수: "지은아, 괜찮다." / "우리 지은이는 정말 착한 아이입니다." | [ROOM], close-up, [C1] gently holding [C4]'s hand on the table, holding back tears | [Camera] static [Dialogue] the old man says in Korean, softly: "지은아, 괜찮다." then: "우리 지은이는 정말 착한 아이입니다." |
| 11 ⭐최고 긴장 | 7 | 영순: "착한 걸로 밥 먹고 살아요? 이 결혼은 없던 걸로 하시죠." | [ROOM], medium shot, [C2] slamming a white money envelope on the table | [Camera] quick push-in [Action] she slaps the envelope down [Dialogue] the woman says in Korean, sharply: "착한 걸로 밥 먹고 살아요? 이 결혼은 없던 걸로 하시죠." [Audio] envelope slap |
| 12 ⭐반전 | 5 | (대사 없음) [툭] | [ROOM], low angle close-up, an old worn taxi name badge falling from a luxury handbag onto the wooden floor | [Camera] slow motion, static [Action] the badge falls and bounces once [Audio] small clack on wood |
| 13 | 7 | 덕수: "…이거, 어디서 나셨습니까?" / "서울 개인택시 김덕수… 이거 제 명찰입니다." | [ROOM], extreme close-up of a faded name badge in [C1]'s rough calloused hand (글자는 편집에서 합성) | [Camera] slow push-in on the badge [Dialogue] the old man says in Korean, trembling: "…이거, 제 명찰입니다." |
| 14 ⭐썸네일 | 4 | 영순: "…뭐라고요?" [헉] | [ROOM], close-up of [C2] frozen in shock, eyes wide, mouth slightly open, pearl necklace | [Camera] static [Dialogue] the woman whispers in Korean, shocked: "…뭐라고요?" |
| 15 회상 | 10 | 덕수: "30년 전 장마철 밤이었죠. 제 작업복으로 아기를 감싸 드렸는데… 그 옷에 명찰이 달려 있었습니다." | 1990s flashback, film grain, warm desaturated, rainy night inside an old Korean taxi, a young taxi driver wrapping a newborn baby in his navy work jacket, rain on windshield | [Camera] slow drift [Action] rain streaks, flickering streetlight [Dialogue] voice-over, old man in Korean, calm: "30년 전 장마철 밤이었죠…" [Audio] heavy rain, baby crying faintly |
| 16 | 9 | 영순: "평생 찾았는데… 이 명찰만 30년을 갖고 다녔어요." / 덕수: "그때 그 아기가 이렇게 컸구나." | [ROOM], medium two-shot, [C2] crying with trembling hands, [C1] smiling warmly at [C3] | [Camera] static [Dialogue] the woman says in Korean, sobbing: "평생 찾았는데… 이 명찰만 30년을 갖고 다녔어요." then the old man says warmly: "그때 그 아기가 이렇게 컸구나." |
| 17 해소 | 10 | 덕수: "사람은 옷으로 보는 게 아니라, 어려울 때 뭘 했는지로 보는 겁니다." / 영순: "우리 며느리… 고맙다." | [ROOM], medium shot, [C1] stopping [C2] from kneeling, then [C2] holding [C4]'s hands, everyone teary-eyed smiling | [Camera] slow pull-out [Dialogue] the old man says in Korean, gently: "사람은 옷으로 보는 게 아니라, 어려울 때 뭘 했는지로 보는 겁니다." then the woman says tearfully: "우리 며느리… 고맙다." |

**엔딩 자막 (2초):** "여러분이 덕수 씨였다면, 이 결혼 허락하셨을까요?"

## 썸네일
- 소스: 14번 컷 (영순의 충격 클로즈업)
- 텍스트: "이게… 왜 여기 있어요?"
