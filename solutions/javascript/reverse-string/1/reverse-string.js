//
// This is only a SKELETON file for the 'Reverse String' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const reverseString = (texto) => {
  let reverso = "";
  for (let letra of texto) {
    console.log(letra);
    reverso = letra + reverso;
  }
  return reverso;
};
