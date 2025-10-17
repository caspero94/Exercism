//
// This is only a SKELETON file for the 'Matrix' exercise. It's been provided as a
// convenience to get you started writing code faster.
//
export class Matrix {
  constructor(matrix) {

    this._matrix = matrix.trim().split("\n").map(n => n.trim().split(" ").map(Number))
    console.log(this._matrix)
  }

  get rows() {
    return this._matrix.map(row => [...row])
  }

  get columns() {
    return this._matrix[0].map((_,colIndex) => this._matrix.map(row=>row[colIndex]))
  }
}
