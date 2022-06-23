function findMissingValue(input) {
  let sum = 0;
  let smallest = Infinity;
  let largest = -Infinity;
  for (let i = 0; i < input.length; i++) {
    sum += input[i];
    smallest = Math.min(smallest, input[i]);
    largest = Math.max(largest, input[i]);
  }
  return (((input.length + 1) * (largest + smallest)) / 2) - sum;
}
