/* 
  Create the function isRotation(str1,str2) that
  returns whether the second string is a rotation of the first.
*/

const strA1 = "ABCD";
const strB1 = "CDAB";
// Explanation: if you start from A in the 2nd string, the letters are in the same order, just rotated
const expected1 = true;

const strA2 = "ABCD";
const strB2 = "CDBA";
// Explanation: all same letters in 2nd string, but out of order
const expected2 = false;

const strA3 = "ABCD";
const strB3 = "BCDAB";
// Explanation: same letters in correct order but there is an extra letter.
const expected3 = false;

/**
 * Determines whether the second string is a rotated version of the first.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} s1
 * @param {string} s2
 * @returns {boolean} Whether the second string is a rotated version of the 1st.
 */
function isRotation(s1, s2) {
    // if lengths not equal, return false
    if (s1.length !== s2.length) 
        return false;
    
    // iterator of s2
    let j = 0;

    // iterate over s2 until char at j equals first char in s1
    while (j < s2.length && s2[j] !== s1[0]) {
        j++;
    }
    // now iterate over s1, while incrementing j in s2
    // check if the chars are equal, if not return false
    // move j in s2 back to 0 if at the end of s2
    for (let i = 0; i < s1.length; i++) {
        if (s1[i] !== s2[j])
            return false;
        j = (j + 1) % s2.length;
    }
    // iteration of s1 complete with rotation true
    return true;
}

console.log(isRotation(strA1,strB1)) //should be true
console.log(isRotation(strA2,strB2)) //should be false
console.log(isRotation(strA3,strB3)) //should be false
