# 03. 캐릭터 고정 시트 프롬프트

> 용도: 등장인물마다 레퍼런스 이미지를 한 장씩 만들어요. 이후 모든 컷에서 이 이미지를 레퍼런스로 넣어 얼굴을 고정해요.
> 입력 변수: `{{SCRIPT_JSON}}` 02단계 결과의 characters

## A. LLM용: 캐릭터 시트 프롬프트 생성

```xml
<role>
너는 AI 이미지 생성용 캐릭터 디자이너야.
</role>

<input>
{{SCRIPT_JSON.characters}}
</input>

<rules>
- 실사풍 한국인. 한국 드라마 스틸컷 느낌.
- 계급 신호를 의상과 소품으로 분명하게 표현해.
  · 부유한 가해자: 진주 목걸이·귀걸이, 트위드나 실크, 스카프, 세팅한 파마머리, 턱을 든 자세
  · 서민 피해자: 니트 카디건, 앞치마, 작업복, 수수한 단발이나 뽀글 파마, 굳은살 있는 손
  · 해결사(회장 등): 짙은 정장, 백발, 온화하지만 위엄 있는 표정
- 얼굴 특징(얼굴형, 주름, 머리 모양, 점)을 구체적으로 적어서 재현성을 높여.
- 실존 인물(배우, 정치인)을 닮게 하거나 이름을 언급하지 마.
- 의상은 에피소드 내내 고정이야. 이후 컷 프롬프트에 그대로 복사해서 쓸 수 있게 짧은 영문 구로 정리해.
</rules>

<output-format>
JSON 배열로만 출력해.
[
  {
    "id": "C1",
    "name": "이름",
    "sheet_prompt": "캐릭터 시트용 영문 프롬프트 전체",
    "identity_tag": "컷 프롬프트에 붙일 짧은 영문 구 (예: 'Deoksu, 63yo Korean taxi driver, short gray hair, tanned wrinkled face, navy work jacket with name badge')",
    "voice": "TTS 목소리 설명"
  }
]
</output-format>
```

## B. 캐릭터 시트 이미지 프롬프트 템플릿 (이미지 모델에 바로 넣는 용도)

```
Photorealistic character reference sheet of {identity}, {age}-year-old Korean {gender}, {face details}, {hair}, wearing {outfit}, {accessories}.
Front-facing medium close-up, neutral expression, soft natural studio lighting, plain light gray background,
Korean TV drama still, 35mm lens, ultra realistic skin texture, 9:16 vertical.
No text, no watermark, no logo.
```

추천 모델: Nano Banana Pro, Seedream, GPT Image, Soul. 마음에 드는 얼굴이 나올 때까지 3~4장 뽑아서 1장을 고르세요.
