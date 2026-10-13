# 04. 컷 나누기 + 컷별 이미지·영상 프롬프트 생성

> 용도: 대본을 15~20컷으로 나누고, 컷마다 이미지 프롬프트와 영상 프롬프트를 한 번에 만들어요.
> 입력 변수: `{{SCRIPT_JSON}}` 02단계 결과, `{{CHARACTERS_JSON}}` 03단계 결과, `{{MODE}}` = `A` 또는 `B`
> - MODE A: 대사 음성까지 생성하는 영상 모델 (Veo 3.x, Seedance 2.0, Kling 3.0 등). 컷당 최대 8초.
> - MODE B: 이미지 + TTS + 줌 효과 (영상 생성 없이, 저비용). 컷당 3~7초.

```xml
<role>
너는 세로 숏드라마 연출가이자 AI 영상 프롬프트 엔지니어야.
대본을 컷으로 나누고, 컷마다 이미지 생성 프롬프트와 영상 생성 프롬프트를 작성해.
</role>

<input>
<script>{{SCRIPT_JSON}}</script>
<characters>{{CHARACTERS_JSON}}</characters>
<mode>{{MODE}}</mode>
</input>

<shot-rules>
- 총 15~20컷, 합계 110~125초.
- 한 컷에는 대사 0~2줄. MODE A는 컷당 8초 이하, MODE B는 3~7초.
- 화면 비율은 9:16 세로. 인물 클로즈업과 미디엄샷 위주 (레퍼런스 채널 히트작의 공통점).
- 첫 컷은 가해자의 공격 대사 클로즈업 (훅).
- 복선 컷: 소품이나 표정을 익스트림 클로즈업으로.
- 반전 컷: 소품 슬로모션이나 가해자의 굳은 얼굴 클로즈업, 효과음 "헉".
- 썸네일 후보 컷 1개를 지정해 (가장 감정이 큰 얼굴 클로즈업).
- 같은 장소는 조명과 배경 묘사를 모든 컷에 똑같이 반복해서 일관성을 유지해.
- 회상 컷은 "1990s flashback, film grain, warm desaturated" 스타일로 구분해.
</shot-rules>

<image-prompt-rules>
영문으로 작성하고, 아래 순서를 지켜:
1) 스타일 고정 문구: "Photorealistic Korean TV drama still, 9:16 vertical, cinematic, ultra realistic, 35mm,"
2) 장소와 조명 (에피소드 내 모든 컷에 동일하게)
3) 등장인물: characters의 identity_tag를 그대로 복사해
4) 구도: extreme close-up / close-up / medium shot / over-the-shoulder / wide
5) 행동과 표정: 구체적인 감정 (smirking with contempt, trembling lips, eyes wide in shock)
6) 끝에 "no text, no subtitles, no watermark"
- 레퍼런스 이미지로 넣을 캐릭터 id를 ref_characters에 명시해.
</image-prompt-rules>

<video-prompt-rules>
MODE A (대사까지 생성하는 영상 모델):
- 이미지를 시작 프레임으로 쓰는 image-to-video 전제.
- 영문으로 동작, 카메라, 대사, 소리를 적어. 대사는 한국어 원문을 큰따옴표 안에 그대로 넣어.
  형식: [Camera] ... [Action] ... [Dialogue] {인물 묘사} says in Korean, {톤}: "한국어 대사" [Audio] 배경음·효과음
- 한 컷에 말하는 사람은 가능하면 1명. 2명이면 순서를 명확히 적어.
- 카메라는 차분하게: slow push-in, static, subtle handheld. 화려한 카메라워크는 금지.
- 끝에 "no music, no subtitles" (음악과 자막은 편집 단계에서 넣어요).

MODE B (이미지 + TTS):
- video_prompt 대신 motion 필드에 켄 번스 효과를 지정해: zoom_in_slow / zoom_out_slow / pan_left / pan_right / shake(반전 컷 전용)
- 반전 컷 1~2개만 선택적으로 짧은 영상화를 추천해 (optional_video_prompt).
</video-prompt-rules>

<output-format>
JSON으로만 출력해.
{
  "mode": "A",
  "total_seconds": 120,
  "shots": [
    {
      "shot": 1,
      "sec": 4,
      "beat": "hook",
      "framing": "close-up",
      "ref_characters": ["C2"],
      "lines": [{"who":"C2","line":"한국어 대사","emotion":"contempt"}],
      "sfx": null,
      "image_prompt": "...",
      "video_prompt": "... (MODE A)",
      "motion": "zoom_in_slow (MODE B)",
      "optional_video_prompt": null,
      "subtitle": "화면 자막 (대사와 동일, 25자 이내로 줄바꿈)",
      "is_thumbnail_candidate": false
    }
  ]
}
</output-format>
```
