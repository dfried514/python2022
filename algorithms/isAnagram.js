function isAnagram(string_a, string_b) {
  // create two new strings, so all chars are lower case
  const sA = string_a.toLowerCase();
  const sB = string_b.toLowerCase();

  // create an object with the counts of each char from string A
  const charCounts_a = {};
  for (const char of sA) { 
    if (char === ' ')
      continue;
    charCounts_a[char] = charCounts_a[char] + 1 || 1;
  }
  // iterate over string B, if char is not in object counts from string A
  // return false
  // else decrement char in object
  // at end object will be empty, return true
  for (const char of sB) {
    if (char === ' ')
      continue;
    if (!charCounts_a[char])
      return false;
    charCounts_a[char]--;
  }
  return true;
}
