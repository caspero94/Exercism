//
// This is only a SKELETON file for the 'RNA Transcription' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const toRna = (dna) => {
  return dna.split("").map(char => DNA_TO_RNA[char]).join("")
};

const DNA_TO_RNA = {
  G: "C",
  C: "G",
  T: "A",
  A: "U",
};