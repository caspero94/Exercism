//
// This is only a SKELETON file for the 'Difference Of Squares' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export class Squares {
  constructor(x) {
    this.x = x;
    this.sum;
  }

  get sumOfSquares() {
    let sum = 0;
    for (let y = 1; y <= this.x; y++) {
      sum += y ** 2;
    }
    return sum;
  }

  get squareOfSum() {
    let sum = 0;
    for (let y = 1; y <= this.x; y++) {
      sum += y;
    }
    return sum ** 2;
  }

  get difference() {
    return this.squareOfSum - this.sumOfSquares;
  }
}
