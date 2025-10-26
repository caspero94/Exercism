//
// This is only a SKELETON file for the 'Armstrong Numbers' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const isArmstrongNumber = (n) => {
  const originalN = BigInt(n);
  const nStr = String(originalN);
  const numDigitos = BigInt(nStr.length);
  let sumaPotencias = BigInt(0);
  for (let i = 0; i < nStr.length; i++) {
    sumaPotencias += BigInt(+nStr[i]) ** numDigitos;
  }
  return sumaPotencias === originalN;
};
