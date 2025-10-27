const COL = {
  black: 0,
  brown: 1,
  red: 2,
  orange: 3,
  yellow: 4,
  green: 5,
  blue: 6,
  violet: 7,
  grey: 8,
  white: 9,
};

export class ResistorColorTrio {
  constructor(trio) {
    if (trio.some((c) => !(c in COL))) throw new Error("invalid color");
    this.value = (COL[trio[0]] * 10 + COL[trio[1]]) * 10 ** COL[trio[2]];
  }

  get label() {
    let unit = "ohms";
    if (this.value >= 1_000_000_000) {
      this.value /= 1_000_000_000;
      unit = "gigaohms";
    } else if (this.value >= 1_000_000) {
      this.value /= 1_000_000;
      unit = "megaohms";
    } else if (this.value >= 1_000) {
      this.value /= 1_000;
      unit = "kiloohms";
    }
    return `Resistor value: ${this.value} ${unit}`;
  }
}
