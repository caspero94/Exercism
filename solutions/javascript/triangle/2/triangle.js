//
// This is only a SKELETON file for the 'Triangle' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export class Triangle {
  constructor(...s) {
    this.s = [...s].sort();
    this.isTriangle = this.s[0] + this.s[1] >= this.s[2] && this.s[0] > 0;
  }

  get isEquilateral() {
    return this.s.every((x) => x === this.s[0] && this.isTriangle);
  }

  get isIsosceles() {
    return new Set(this.s).size <= 2 && this.isTriangle;
  }

  get isScalene() {
    return new Set(this.s).size === 3 && this.isTriangle;
  }
}
