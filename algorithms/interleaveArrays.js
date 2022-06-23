function interleaveArrays(arrayA, arrayB) {
  const res = [];
  const longest = arrayA.length > arrayB.length ? arrayA.length : arrayB.length;
  for (let i = 0; i < longest; i++) {
    if (arrayA[i]) res.push(arrayA[i]);
    if (arrayB[i]) res.push(arrayB[i]);
  }
  return res;
}
