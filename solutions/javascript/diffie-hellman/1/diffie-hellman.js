//
// This is only a SKELETON file for the 'Diffie Hellman' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

const isPrime = (n) => {
  if (n <= 1) return false;
  for (let i = 2; i <= Math.sqrt(n); i++) {
    if (n % i === 0) return false;
  }
  return true;
};

export class DiffieHellman {
  constructor(p, g) {
    if (!isPrime(p) || !isPrime(g) || g >= p) throw new Error();
    this.g = g;
    this.p = p;
  }

  getPublicKey(privateKey) {
    if (privateKey <= 1 || privateKey >= this.p) throw new Error();
    return this.g ** privateKey % this.p;
  }

  getSecret(theirPublicKey, myPrivateKey) {
    return theirPublicKey ** myPrivateKey % this.p;
  }

  static getPrivateKey(p) {
    return Math.floor(Math.random() * (p - 2)) + 2;
  }
}
