// 주어진 키로 객체에서 값을 찾는 함수
function findItemByKey(obj, key) {
  return obj[key];
}

// 타입 안전성을 고려한 함수
function add(num1, num2) {
  if (typeof num1 !== "number" || typeof num2 !== "number") return null;
  if (num2 === 0 || num2 === +0 || num2 === -0) return null;
  const divideNum = num1 / num2;
  if (divideNum === Infinity || divideNum === -Infinity) return null;
  return divideNum;
}

// 문자열을 전처리하는 함수
function convertStr(str, fn) {
  const newStr = fn(str);
  return newStr === "" ? "-" : newStr;
}
