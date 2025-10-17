//
// This is only a SKELETON file for the 'High Scores' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export class HighScores {
  constructor(puntuaciones) {
    this.puntuaciones = puntuaciones;
  }

  get scores() {
    return this.puntuaciones;
  }

  get latest() {
    return this.puntuaciones[this.puntuaciones.length - 1];
  }

  get personalBest() {
    return Math.max(...this.puntuaciones);
  }

  get personalTopThree() {
    return [...this.puntuaciones].sort((a, b) => b - a).slice(0, 3);
  }
}
