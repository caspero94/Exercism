//
// This is only a SKELETON file for the 'Resistor Color Duo' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const decodedValue = (colors) => {
  if (colors.length > 2) colors = colors.slice(0, 2);
  let result = "";
  for (const color of colors) result += COLORS.indexOf(color);
  return Number(result);
};

const COLORS = [
  "black",
  "brown",
  "red",
  "orange",
  "yellow",
  "green",
  "blue",
  "violet",
  "grey",
  "white",
];
