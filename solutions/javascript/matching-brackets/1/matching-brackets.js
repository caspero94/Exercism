//
// This is only a SKELETON file for the 'Matching Brackets' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

// []{}()

export const isPaired = (code) => {
  const pares = { "[": "]", "{": "}", "(": ")" };
  let codeClean = [...code.replace(/[^(){}[\]]/g, "").split("")];
  const acum = [];
  for (let simbol of codeClean) {
    if ("([{".includes(simbol)) {
      acum.push(pares[simbol]);
    } else {
      if (simbol !== acum.pop()) return false;
    }
  }
  if (acum.length > 0) return false;
  return true;
};
