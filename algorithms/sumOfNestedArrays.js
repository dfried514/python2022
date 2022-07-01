// write a function sumOfNestedArrays which accepts one parameter, input, an array
// return the sum of all numbers in that array...
// ... unless one of the array elements is itself an array, in which case you
// should add to your sum all of the numbers in that array...
// ... unless one of that array's elements is itself an array, in which case you
// should add all of that array's numbers to your sum... and so on, and so on

// hint: you'll need to be able to determine if an element is or is not a number,
// or in general, determine what type of data something is
// another hint: remember that this is a recursive problem

function sumOfNestedArrays(input) {
  let sum = 0;

  const rec = input => {
      input.forEach(val => {
        if (Array.isArray(val))
          rec(val);
        else
          sum += val;
      })
  }
  rec(input);
  return sum;
}

console.log(sumOfNestedArrays([1, 2, 3, 4, 5])) // returns 15
console.log(sumOfNestedArrays([1, 2, 3, 4, [1, 1, 2]])) // returns 14
console.log(sumOfNestedArrays([[1, 2], [3, 4], [5, 6], [7, 8]])) // returns 36
console.log(sumOfNestedArrays([1, [1, 2, 3], [7, [5, 4, 1]], [21, -7, 1], [1, 13, 131]])) // returns 184
