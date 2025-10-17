//
// This is only a SKELETON file for the 'Pangram' exercise. It's been provided as a
// convenience to get you started writing code faster.
//


export const isPangram = (sentence) => {
  const alphabet = new Set('abcdefghijklmnopqrstuvwxyz');
  for (const letter of sentence){
    alphabet.delete(letter.toLowerCase())
  }
  return alphabet.size === 0 ? true : false
};
