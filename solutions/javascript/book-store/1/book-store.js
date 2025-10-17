//
// This is only a SKELETON file for the 'BookStore' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export function cost(books) {
  const frequencies = {};
  books.forEach((book) => (frequencies[book] = (frequencies[book] || 0) + 1));
  const sortedFreqs = Object.values(frequencies).sort((a, b) => b - a);

  const calculateMinPrice = (freqs, memo) => {
    if (!freqs.length) return 0;
    const key = freqs.join();
    if (memo[key]) return memo[key];

    let minPrice = Infinity;
    for (let size = Math.min(5, freqs.length); size > 0; size--) {
      const price = size * 800 * (1 - [0, 0, 0.05, 0.1, 0.2, 0.25][size]);
      const remaining = freqs
        .map((val, idx) => (idx < size ? val - 1 : val))
        .filter((val) => val > 0)
        .sort((a, b) => b - a);
      minPrice = Math.min(minPrice, price + calculateMinPrice(remaining, memo));
    }
    return (memo[key] = minPrice);
  };

  return calculateMinPrice(sortedFreqs, {});
}
