//
// This is only a SKELETON file for the 'Protein Translation' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

const RNA = {
  AUG: "Methionine",
  UUU: "Phenylalanine",
  UUC: "Phenylalanine",
  UUA: "Leucine",
  UUG: "Leucine",
  UCU: "Serine",
  UCC: "Serine",
  UCA: "Serine",
  UCG: "Serine",
  UAU: "Tyrosine",
  UAC: "Tyrosine",
  UGU: "Cysteine",
  UGC: "Cysteine",
  UGG: "Tryptophan",
  UAA: "STOP",
  UAG: "STOP",
  UGA: "STOP",
};

export const translate = (rna = null) => {
  let proteins = [];
  if (!rna) return proteins;
  for (let i = 0; i < rna.length; i += 3) {
    let element = RNA[rna.slice(i, i + 3)];
    if (!element) throw new Error("Invalid codon");
    if (element === "STOP") break;
    proteins.push(element);
  }
  return proteins;
};
