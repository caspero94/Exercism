export class Palindromes {
  static generate({ minFactor, maxFactor }) {
    if (minFactor > maxFactor) throw new Error("min must be <= max");

    const palindromesMap = new Map();

    for (let i = minFactor; i <= maxFactor; i++) {
      for (let j = i; j <= maxFactor; j++) {
        const product = i * j;
        const str = product.toString();
        if (str === str.split("").reverse().join("")) {
          if (!palindromesMap.has(product)) {
            palindromesMap.set(product, []);
          }
          palindromesMap.get(product).push([i, j]);
        }
      }
    }

    const palindromes = Array.from(palindromesMap.keys());
    const palindromeMin = palindromes.length ? Math.min(...palindromes) : null;
    const palindromeMax = palindromes.length ? Math.max(...palindromes) : null;

    return {
      smallest: {
        value: palindromeMin,
        factors:
          palindromeMin !== null ? palindromesMap.get(palindromeMin) : [],
      },
      largest: {
        value: palindromeMax,
        factors:
          palindromeMax !== null ? palindromesMap.get(palindromeMax) : [],
      },
    };
  }
}
