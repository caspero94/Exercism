//
// This is only a SKELETON file for the 'Anagram' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const findAnagrams = (word, anagrams) => {
  let words = word.toLowerCase().split("").sort().join("");
  const res = [];
  for (let ana of anagrams) {
    console.log(ana);
    if (
      ana.toLowerCase() !== word.toLowerCase() &&
      ana.toLowerCase().split("").sort().join("") === words
    )
      res.push(ana);
  }
  return res;
};
