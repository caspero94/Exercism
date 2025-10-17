//
// This is only a SKELETON file for the 'Perfect Numbers' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const classify = (x) => {
  if (x < 1)
    throw new Error("Classification is only possible for natural numbers.");
  if (x === 1) return "deficient";
  let y = x;
  let numbers = [1];
  for (let n = 2; n < x; n++) {
    if (x % n === 0) {
      numbers.push(n);
    }
  }

  y = numbers.reduce((acc, cur) => acc + cur);
  return y === x ? "perfect" : y < x ? "deficient" : "abundant";
};
