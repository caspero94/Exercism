export class Robot {
  static usedNames = new Set();
  static availableNames = [];

  #name;

  constructor() {
    if (Robot.availableNames.length === 0) Robot.generateAllNames();
    this.#assignName();
  }

  get name() {
    return this.#name;
  }

  reset() {
    if (Robot.availableNames.length === 0) {
      throw new Error("No more names available");
    }
    this.#assignName();
  }

  #assignName() {
    if (Robot.availableNames.length === 0) {
      throw new Error("No more names available");
    }
    const newName = Robot.availableNames.pop();
    this.#name = newName;
    Robot.usedNames.add(newName);
  }

  static generateAllNames() {
    const names = new Array(26 * 26 * 1000);
    let idx = 0;
    for (let i = 0; i < 26; i++) {
      const a = String.fromCharCode(65 + i);
      for (let j = 0; j < 26; j++) {
        const b = String.fromCharCode(65 + j);
        for (let k = 0; k < 1000; k++) {
          names[idx++] = a + b + String(k).padStart(3, "0");
        }
      }
    }

    for (let i = names.length - 1; i > 0; i--) {
      const r = Math.floor(Math.random() * (i + 1));
      const tmp = names[i];
      names[i] = names[r];
      names[r] = tmp;
    }

    Robot.availableNames = names;
  }
}

Robot.releaseNames = () => {
  Robot.availableNames = [];
  Robot.usedNames.clear();
};
