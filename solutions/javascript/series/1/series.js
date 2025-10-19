//
// This is only a SKELETON file for the 'Series' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export class Series {
  constructor(series) {
    this.series = series.split("").map(Number);
  }

  slices(sliceLength) {
    if (this.series.length === 0) throw new Error("series cannot be empty");
    if (sliceLength === 0) throw new Error("slice length cannot be zero");
    if (sliceLength < 0) throw new Error("slice length cannot be negative");
    if (this.series.length < sliceLength)
      throw new Error("slice length cannot be greater than series length");
    let res = [];
    let iter = [];
    for (let item of this.series) {
      iter.push(item);
      if (iter.length === sliceLength) {
        res.push([...iter]);
        iter.shift();
      }
    }
    return res;
  }
}
