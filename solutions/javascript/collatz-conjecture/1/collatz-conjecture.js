//
// This is only a SKELETON file for the 'Collatz Conjecture' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const steps = (x) => {
  if (x < 1) throw new Error("Only positive integers are allowed");
  let step = 0;
  while (x > 1) {
    x = x % 2 === 0 ? x / 2 : x * 3 + 1;
    step++;
  }
  return step;
};
