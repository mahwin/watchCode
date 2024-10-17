export function version0(msg) {
  return `<task-description>
프로그래밍 과정에서 개발자가 놓치기 쉬운 실수나 에러를 검증하려고해.
나는 검증에 사용할 리스트를 갖고 있고, 해당 리스트를 기준으로 코드가 잘 작성했는 지를 체크할 사람이 필요해.
체크 단위도 함수를 기준으로 진행했으면 좋겠어!!
</task-description>

<input-indicator>
너가 검증하는 역할을 맡게 될거야.
</input-indicator>

<current-input>
${msg}
</current-input>

<check-list>
[] null, undefined를 적절하게 처리 했는가
[] NaN, Infinity를 적절하게 처리 했는가
[] 빈 문자열일 경우 "-"를 반환하는가
[] === 비교만을 사용하는가
[] 파라메타에 대한 타입 가드를 적용했는가
</check-list>

<output-Iidicator>
함수 단위로 내가 알려준 check-list에 맞춰서 너가 코드를 해석하고 리스트 목록에 O나 X를 적어줬으면 좋겠어.
</output-Iidicator>

<output>

함수 이름 1
[O] null, undefined를 적절하게 처리 했는가
[X] NaN, Infinity를 적절하게 처리 했는가
[O] 빈 문자열일 경우 "-"를 반환하는가
[O] === 비교만을 사용하는가
[O] 파라메타에 대한 타입 가드를 적용했는가

함수 이름 2
[O] null, undefined를 적절하게 처리 했는가
[X] NaN, Infinity를 적절하게 처리 했는가
[O] 빈 문자열일 경우 "-"를 반환하는가
[O] === 비교만을 사용하는가
[O] 파라메타에 대한 타입 가드를 적용했는가

</output>

<example-1>
function findElement(arrs){ const targetIdx = arrs.indexOf(); return arrs[targetIdx] }
</example-1>

<example-1-output>
[X] null, undefined를 적절하게 처리 했는가
[O] NaN, Infinity를 적절하게 처리 했는가
[O] 빈 문자열일 경우 "-"를 반환하는가
[O] === 비교만을 사용하는가
[X] 파라메타에 대한 타입 가드를 적용했는가
</example-1-output>

<example-2>
function divide(입력한_수, 나눈_수){ return 입력한 / 나눈_수; }
</example-2>

<example-2-output>
[O] null, undefined를 적절하게 처리 했는가
[X] NaN, Infinity를 적절하게 처리 했는가
[O] 빈 문자열일 경우 "-"를 반환하는가
[O] === 비교만을 사용하는가
[X] 파라메타에 대한 타입 가드를 적용했는가
</example-2-output>

<example-3>
function stringParser(originString){ return originString.split(',').join('.').trim();  }
</example-3>

<example-3-output>
[O] null, undefined를 적절하게 처리 했는가
[O] NaN, Infinity를 적절하게 처리 했는가
[X] 빈 문자열일 경우 "-"를 반환하는가
[O] === 비교만을 사용하는가
[X] 파라메타에 대한 타입 가드를 적용했는가
</example-3-output>

<example-4>
function stringAdd (strA, strB){ return strA + strB; }
</example-4>

<example-4-output>
[O] null, undefined를 적절하게 처리 했는가
[O] NaN, Infinity를 적절하게 처리 했는가
[X] 빈 문자열일 경우 "-"를 반환하는가
[O] === 비교만을 사용하는가
[X] 파라메타에 대한 타입 가드를 적용했는가
</example-4-output>

<example-5>
function eqaul(a,b){ return a == b }
</example-5>

<example-5-output>
[O] null, undefined를 적절하게 처리 했는가
[O] NaN, Infinity를 적절하게 처리 했는가
[O] 빈 문자열일 경우 "-"를 반환하는가
[X] === 비교만을 사용하는가
[X] 파라메타에 대한 타입 가드를 적용했는가
</example-5-output>`;
}
