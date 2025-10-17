//
// This is only a SKELETON file for the 'Triangle' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export class Triangle {
  constructor(...sides) {
    this.sides = [...sides].sort();
    this.isTriangle = this.sides[0] + this.sides[1] >= this.sides[2];
  }

  get isEquilateral() {
    return this.sides.every((x) => x === this.sides[0] && x > 0.0);
  }

  get isIsosceles() {
    return new Set(this.sides).size <= 2 && this.isTriangle;
  }

  get isScalene() {
    return new Set(this.sides).size === 3 && this.isTriangle;
  }
}
