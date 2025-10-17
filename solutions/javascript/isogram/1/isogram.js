//
// This is only a SKELETON file for the 'Isogram' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const isIsogram = (iso) => {
  const clean = iso.toLowerCase().replace(/[^a-zA-Z]/g, "");
  return clean.length === new Set(clean).size;
};
