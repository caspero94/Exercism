//
// This is only a SKELETON file for the 'Reverse String' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const reverseString = (str) =>
  (str.match(/(\P{Mark}\p{Mark}*|[\p{Mark}]+)/gu) || []).reverse().join("");
