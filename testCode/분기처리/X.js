function handleThreeBooleanProperties(prop1, prop2, prop3) {
  if (!prop1 && !prop2 && !prop3) {
    return "케이스 1: 모든 속성이 false입니다.";
  } else if (!prop1 && !prop2 && prop3) {
    return "케이스 2: 속성3만 true입니다.";
  } else if (!prop1 && prop2 && !prop3) {
    return "케이스 3: 속성2만 true입니다.";
  } else if (!prop1 && prop2 && prop3) {
    return "케이스 4: 속성2와 속성3이 true입니다.";
  } else if (prop1 && !prop2 && !prop3) {
    return "케이스 5: 속성1만 true입니다.";
  } else if (prop1 && !prop2 && prop3) {
    return "케이스 6: 속성1과 속성3이 true입니다.";
  } else if (prop1 && prop2 && prop3) {
    return "케이스 8: 모든 속성이 true입니다.";
  }
}
