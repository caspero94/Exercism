export const primeFactors = (num) => {
  let primes = [];
  for (let i = 2; i <= num; ) {
    num % i === 0 ? primes.push(i) && (num /= i) : i++;
  }
  return primes;
};
