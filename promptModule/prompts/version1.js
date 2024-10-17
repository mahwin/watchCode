export function version1(msg) {
  return `<task-description>
프로그래밍 과정에서 개발자가 놓치기 쉬운 실수나 에러를 검증하려고해.
특히나, null과 undefined을 제대로 처리했는 지가 중요해. 
예를 들면 obj[key]를 했는데 key가 있는지 없는지 먼저 확인하는 코드가 더 안전하잖아? 
이런 부분을 꼼꼼하게 검증해줘
</task-description>

<input-indicator>
너가 검증하는 역할을 맡게 될거야.
</input-indicator>

<current-input>
${msg}
</current-input>

<output>
함수 이름 1
obj[key].map에서 obj[key]가 null이나 undefined나 array가 아닌 경우에 에러가 발생할 수 있습니다.
</output>

<example-1>
function findElement(arrs){ const targetIdx = arrs.indexOf(); return arrs[targetIdx] }
</example-1>

<example-1-output>
findElement
arrs.indexOf()
-> arrs가 array가 아닌 경우에 에러가 발생할 수 있습니다.
arrs[targetIdx]
-> targetIdx가 arrs의 인덱스를 벗어나는 경우에 에러가 발생할 수 있습니다.
</example-1-output>`;
}
