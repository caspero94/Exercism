export class Palindromes {
  static generate(factors) {
    if (factors.minFactor > factors.maxFactor)
      throw new Error("min must be <= max");
    const palindromes = [];
    const factores = {};

    for (let i = factors.minFactor; i <= factors.maxFactor; i++) {
      for (let j = i; j <= factors.maxFactor; j++) {
        let product = i * j;
        if (String(product) === String(product).split("").reverse().join("")) {
          palindromes.push(product);
          if (!(product in factores)) {
            factores[product] = [];
          }
          factores[product].push([i, j]);
        }
      }
    }
    const palindromeMin = palindromes.length ? Math.min(...palindromes) : null;
    const palindromeMax = palindromes.length ? Math.max(...palindromes) : null;

    return {
      smallest: {
        value: palindromeMin,
        factors: palindromeMin !== null ? factores[palindromeMin] : [],
      },
      largest: {
        value: palindromeMax,
        factors: palindromeMax !== null ? factores[palindromeMax] : [],
      },
    };
  }
}
