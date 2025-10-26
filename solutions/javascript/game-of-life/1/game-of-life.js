//
// This is only a SKELETON file for the 'Conway's Game of Life' exercise. It's been provided
// as a convenience to get you started writing code faster.
//

export class GameOfLife {
  constructor(m) {
    this.m = m;
  }

  tick() {
    const newState = this.m.map((row) => [...row]);
    const movimientos = [[-1, -1],[-1, 0],[-1, 1],[0, -1],[0, 1],[1, -1],[1, 0],[1, 1],];
    for (let x = 0; x < this.m.length; x++) {
      for (let y = 0; y < this.m[x].length; y++) {
        const vecinos = movimientos.reduce((sum, [dx, dy]) => sum + (this.m[x + dx]?.[y + dy] ?? 0),0);
        if (vecinos === 3 || (this.m[x][y] === 1 && vecinos === 2))newState[x][y] = 1;
        else newState[x][y] = 0;
      }
    }
    this.m = newState;
  }
  state = () => this.m;
}
