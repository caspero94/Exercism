//
// This is only a SKELETON file for the 'Grade School' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export class GradeSchool {
  constructor() {
    this.school = {};
  }
  roster() {
    return Object.entries(this.school)
      .sort(([k1, v1], [k2, v2]) => {
        if (v1 !== v2) return v1 - v2;
        return k1.localeCompare(k2);
      })
      .map(([k]) => k);
  }

  add(student, grade) {
    if (this.school[student]) {
      return false;
    } else {
      this.school[student] = grade;
      return true;
    }
  }

  grade(curso) {
    return Object.entries(this.school)
      .filter(([_, value]) => value === curso)
      .map(([k]) => k)
      .sort();
  }
}
