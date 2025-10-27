export class Palindromes {
  static generate(factors) {
    const minFactor = factors.minFactor;
    const maxFactor = factors.maxFactor;

    if (minFactor > maxFactor) throw new Error("min must be <= max");

    let smallest = null;
    let largest = null;

    const smallestFactors = [];
    const largestFactors = [];

    // Calcula los límites de productos posibles
    const minProduct = minFactor * minFactor;
    const maxProduct = maxFactor * maxFactor;

    // Función para verificar si un número está en rango y tiene factor en rango
    const addFactors = (p, factorList) => {
      for (let i = minFactor; i <= Math.floor(Math.sqrt(p)); i++) {
        if (p % i === 0) {
          const j = p / i;
          if (j >= minFactor && j <= maxFactor) {
            factorList.push([i, j]);
          }
        }
      }
    };

    // Generar palíndromos de forma eficiente
    const generatePalindromes = (min, max) => {
      const palindromes = [];
      const minLen = String(min).length;
      const maxLen = String(max).length;

      for (let len = minLen; len <= maxLen; len++) {
        const halfLen = Math.ceil(len / 2);

        const start = 10 ** (halfLen - 1);
        const end = 10 ** halfLen - 1;

        for (let i = start; i <= end; i++) {
          const s = i.toString();
          const pal =
            len % 2 === 0
              ? parseInt(s + s.split("").reverse().join(""))
              : parseInt(s + s.slice(0, -1).split("").reverse().join(""));
          if (pal >= min && pal <= max) palindromes.push(pal);
        }
      }

      return palindromes;
    };

    const palindromes = generatePalindromes(minProduct, maxProduct);

    for (const p of palindromes) {
      const tempFactors = [];
      addFactors(p, tempFactors);

      if (tempFactors.length) {
        if (!smallest || p < smallest) {
          smallest = p;
          smallestFactors.length = 0;
          smallestFactors.push(...tempFactors);
        }
        if (!largest || p > largest) {
          largest = p;
          largestFactors.length = 0;
          largestFactors.push(...tempFactors);
        }
      }
    }

    return {
      smallest: {
        value: smallest ?? null,
        factors: smallestFactors,
      },
      largest: {
        value: largest ?? null,
        factors: largestFactors,
      },
    };
  }
}
