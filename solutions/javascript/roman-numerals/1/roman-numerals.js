//
// This is only a SKELETON file for the 'Roman Numerals' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

const ROMANOS = { M: 1000, CM: 900, D: 500, CD: 400, C: 100, XC: 90, L: 50, XL: 40, X: 10, IX: 9, V: 5, IV: 4, I: 1, };

export const toRoman = (number) => {
  let output = "";
  while (number > 0) {
    for (const [key, value] of Object.entries(ROMANOS)) {
      if (value <= number) {
        output += key;
        number -= value;
        break;
      }
    }
  }
  return output;
};
