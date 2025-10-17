//
// This is only a SKELETON file for the 'Raindrops' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const convert = (x) => {
  let res = "";
  if (x % 3 === 0) res += "Pling";
  if (x % 5 === 0) res += "Plang";
  if (x % 7 === 0) res += "Plong";
  return res || x.toString();
};
