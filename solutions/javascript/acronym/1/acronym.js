//
// This is only a SKELETON file for the 'Acronym' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const parse = (test, acro = "") => {
  test = test.replace(/[\s\-_]+/g, " ").split(" ");
  for (let word of test) acro += word[0].toUpperCase();
  return acro;
};
