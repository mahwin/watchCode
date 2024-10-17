function joinTropicalFruits(obj) {
  if (!obj || typeof obj !== "object") {
    return "열대과일이 없습니다.";
  }

  const tropicalFruits = obj.열대과일;
  if (
    !Array.isArray(tropicalFruits.values) ||
    tropicalFruits.values.length === 0
  ) {
    return "열대과일 데이터가 없습니다.";
  }

  return tropicalFruits.join(",");
}
