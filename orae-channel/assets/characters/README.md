# 캐릭터 이미지 보관함

확정된 캐릭터 이미지입니다. 이미지 생성 프롬프트는 `docs/06_캐릭터바이블.md`에 있습니다. 새 그림을 만들 때 해당 캐릭터 파일을 **참조 이미지로 첨부**합니다.

| 파일 | 내용 | 크기 |
|---|---|---|
| `orae_master.png` | 오래 박사 정면 전신 (모든 오래 박사 생성의 참조 이미지) | |
| `orae_expressions.png` | 표정 5종: 미소 / 놀람 / 검지 경고 / 턱 괴고 생각 / 윙크 엄지척 | 2000×682 |
| `orae_poses.png` | 포즈 6종: 화이트보드 설명 / 자료 보며 생각 / 놀라며 가리킴 / 동전·태블릿(경제) / 가슴에 손 인사 / 엄지척 | 1536×1024 |
| `orae_icon.png` | 채널 아이콘 (크림색 원 배경) | 1254×1254 |
| `man_sheet.png` | 50대 남성: 전신, 4방향, 표정 6(미소·맛있음·놀람·걱정·피곤·웃음), 동작 6(컵·밥·배 아픔·허리 통증·통장·엄지척) | 1536×1024 |
| `woman_sheet.png` | 50대 여성: 전신, 4방향, 표정 6, 동작 6(컵·밥·배 아픔·거울·열감·휴대폰) | 1536×1024 |
| `man_master.png`, `woman_master.png` | 시트에서 잘라낸 정면 전신 (참조 첨부용, 저해상도) | 307×614 |
| `original/` | 채도 보정 전 오래 박사 원본 4개 (되돌릴 때만 사용, 생성 참조로 첨부하지 않음) | |

오래 박사 파일 4개는 2026-10-16에 사람 캐릭터와 색을 맞추려고 채도를 낮췄습니다(B안). 새 그림을 만들 때는 이 폴더의 보정본을 첨부합니다.

## 낱장 PNG (`cutouts/`, 배경 투명 46장)
편집 도구에 바로 올려 쓰는 파일입니다. 시트에서 `python3 tools/cutout.py`로 잘라 만들었습니다. 시트를 고해상도로 바꾸면 같은 명령으로 다시 만듭니다.

| 폴더 | 파일 | 내용 | 크기(px) | 쓰는 곳 |
|---|---|---|---|---|
| deer | `deer_00_basic.png` | 오래 박사 기본 전신 | 732x1495 | 기본 등장, 목차 화면 |
| deer | `deer_face_01_smile.png` | 미소 | 380x474 | 번호 카드, 엔딩 |
| deer | `deer_face_02_surprised.png` | 놀람 | 369x473 | 결과 공개, 썸네일 |
| deer | `deer_face_03_warning.png` | 검지 경고 | 399x476 | 하면 안 되는 습관 |
| deer | `deer_face_04_thinking.png` | 턱 괴고 생각 | 378x475 | 질문으로 넘어갈 때 |
| deer | `deer_face_05_wink.png` | 윙크 엄지척 | 399x476 | 정답 공개, 정리 카드 |
| deer | `deer_pose_01_board.png` | 화이트보드 설명 | 426x489 | 연구·그래프 설명 |
| deer | `deer_pose_02_report.png` | 자료 보며 생각 | 279x494 | 자료 소개 |
| deer | `deer_pose_03_point.png` | 놀라며 가리킴 | 368x494 | 의외의 사실, 다음 항목 안내 |
| deer | `deer_pose_04_money.png` | 동전·태블릿 (경제) | 359x511 | 경제 편 |
| deer | `deer_pose_05_bow.png` | 가슴에 손 인사 | 264x506 | 엔딩 인사 |
| deer | `deer_pose_06_thumbsup.png` | 엄지척 | 263x510 | 정리, 추천 |
| man | `man_00_basic.png` | 남성 기본 전신 | 256x612 | 기본 등장 |
| man | `man_turn_1_front.png` | 정면 | 173x394 | 장면 구성 (방향 맞추기) |
| man | `man_turn_2_three_quarter.png` | 3/4 측면 | 164x397 | 장면 구성 (방향 맞추기) |
| man | `man_turn_3_side.png` | 옆모습 | 113x395 | 장면 구성 (방향 맞추기) |
| man | `man_turn_4_back.png` | 뒷모습 | 174x395 | 장면 구성 (방향 맞추기) |
| man | `man_face_01_smile.png` | 미소 | 202x213 | 평소 반응 |
| man | `man_face_02_yummy.png` | 맛있음 | 224x214 | 먹는 장면 |
| man | `man_face_03_surprised.png` | 놀람 | 204x210 | 훅, 썸네일 놀람 |
| man | `man_face_04_worried.png` | 걱정 | 204x203 | 걱정되는 상황 |
| man | `man_face_05_tired.png` | 피곤 | 206x199 | 피로·수면 주제 |
| man | `man_face_06_laugh.png` | 활짝 웃음 | 208x206 | 정답 순간, 좋은 변화 |
| man | `man_act_01_drink.png` | 컵으로 마시기 | 198x395 | 커피·차 마시는 장면 |
| man | `man_act_02_eat.png` | 밥 먹기 | 188x391 | 식사 장면 |
| man | `man_act_03_stomachache.png` | 배 아픔 | 202x382 | 장·소화 주제 |
| man | `man_act_04_backpain.png` | 허리 통증 | 227x384 | 허리·관절 주제 |
| man | `man_act_05_passbook.png` | 통장 보며 걱정 | 180x392 | 경제 편 |
| man | `man_act_06_thumbsup.png` | 엄지척 | 204x393 | 정리, 좋은 변화 |
| woman | `woman_00_basic.png` | 여성 기본 전신 | 257x615 | 기본 등장 |
| woman | `woman_turn_1_front.png` | 정면 | 167x402 | 장면 구성 (방향 맞추기) |
| woman | `woman_turn_2_three_quarter.png` | 3/4 측면 | 147x404 | 장면 구성 (방향 맞추기) |
| woman | `woman_turn_3_side.png` | 옆모습 | 124x397 | 장면 구성 (방향 맞추기) |
| woman | `woman_turn_4_back.png` | 뒷모습 | 171x400 | 장면 구성 (방향 맞추기) |
| woman | `woman_face_01_smile.png` | 미소 | 199x217 | 평소 반응 |
| woman | `woman_face_02_yummy.png` | 맛있음 | 216x215 | 먹는 장면 |
| woman | `woman_face_03_surprised.png` | 놀람 | 205x214 | 훅, 썸네일 놀람 |
| woman | `woman_face_04_worried.png` | 걱정 | 196x211 | 걱정되는 상황 |
| woman | `woman_face_05_tired.png` | 피곤 | 206x209 | 피로·수면 주제 |
| woman | `woman_face_06_laugh.png` | 활짝 웃음 | 220x215 | 정답 순간, 좋은 변화 |
| woman | `woman_act_01_drink.png` | 컵으로 마시기 | 183x393 | 커피·차 마시는 장면 |
| woman | `woman_act_02_eat.png` | 밥 먹기 | 175x387 | 식사 장면 |
| woman | `woman_act_03_stomachache.png` | 배 아픔 | 188x382 | 장·소화 주제 |
| woman | `woman_act_04_mirror.png` | 거울 보기 (피부) | 180x388 | 피부 주제 |
| woman | `woman_act_05_hotflash.png` | 열감 (갱년기) | 199x390 | 갱년기 주제 |
| woman | `woman_act_06_phone.png` | 휴대폰 보기 | 191x390 | 정보 찾아보는 장면 |

**크기 주의:** 원래 크기보다 크게 키우면 흐려집니다. 사람 얼굴(약 210px)은 작게만 씁니다.

## 남은 일
- 시트 속 포즈 하나가 세로 250~350px입니다. 영상에 크게 쓰려면 업스케일하거나 낱장으로 다시 뽑습니다.
- 고해상도 시트가 생기면 `python3 tools/cutout.py`로 낱장을 다시 만듭니다.
