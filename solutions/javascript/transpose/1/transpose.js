//
// This is only a SKELETON file for the 'Transpose' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const transpose = (input) => {
  let output = [];
  for (let i = 0; i < input.length; i++) {
    for (let j = 0; j < input[i].length; j++) {
      let rowLength = 0;
      let element = input[i][j];

      if (output[j]) {
        rowLength = output[j].length;
      }
      if (i > rowLength) {
        element = element.padStart(i - rowLength + 1, " ");
      }
      output[j] ? (output[j] += element) : (output[j] = element);
    }
  }
  return output;
};

/*
  if (input.length === 0) return input;
  const maxLen = Math.max(...input.map((x) => x.length));
  console.log(maxLen);
  //const inputClean = input.map((x) => x.padEnd(maxLen, " "));
  //console.log(inputClean);
  let output = [];
  for (let item of input) {
    for (let ind = 0; ind < maxLen; ind++) {
      if (ind === maxLen - 1) {
        output[ind] = (output[ind] ?? "") + (item[ind] ?? "");
      } else {
        output[ind] = (output[ind] ?? "") + (item[ind] ?? " ");
      }
    }
  }
  output[output.length - 1] = output[output.length - 1];
  return output;
*/
