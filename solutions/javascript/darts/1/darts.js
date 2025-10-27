//
// This is only a SKELETON file for the 'Darts' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const score = (x, y) => {
  let distance = Math.sqrt(x * x + y * y);
  return distance > 10 ? 0 : distance > 5 ? 1 : distance > 1 ? 5 : 10;
};
