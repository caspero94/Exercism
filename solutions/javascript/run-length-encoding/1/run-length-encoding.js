//
// This is only a SKELETON file for the 'Run Length Encoding' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const encode = (text) => {
  let result = "";
  let count = 1;
  for (let i = 0; i < text.length; i++) {
    if (text[i] !== text[i + 1]) {
      if (count > 1) {
        result += count;
      }
      result += text[i];
      count = 1;
    } else count++;
  }
  return result;
};

export const decode = (text) => {
  let res = "";
  let n = "";
  for (let i = 0; i < text.length; i++) {
    if (/[0-9]/.test(text[i])) {
      n += String(text[i]);
    } else {
      res += text[i];
      for (let j = 1; j < Number(n); j++) {
        res += text[i];
      }
      n = "";
    }
  }
  return res;
};
