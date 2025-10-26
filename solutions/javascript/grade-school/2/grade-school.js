//
// This is only a SKELETON file for the 'Grade School' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export class GradeSchool {
  constructor() {
    this.school = {};
  }
  roster() {
    return Object.entries(this.school).sort(([k1, v1], [k2, v2]) => v1 - v2 || k1.localeCompare(k2)).map(([k]) => k);
  }

  add(student, grade) {
    return this.school[student] ? false: ((this.school[student] = grade), true);
  }

  grade(curso) {
    return Object.keys(this.school).filter((student) => this.school[student] === curso).sort();
  }
}
