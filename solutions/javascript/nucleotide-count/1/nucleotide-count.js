export const countNucleotides = (s) => {
  if (![...s].every((c) => "ACGT".includes(c)))throw new Error("Invalid nucleotide in strand");
  return ["A", "C", "G", "T"].map((x) => [...s].filter((c) => c === x).length).join(" ");
};
