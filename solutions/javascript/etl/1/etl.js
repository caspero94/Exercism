//
// This is only a SKELETON file for the 'ETL' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const transform = (dic) => {
  const res = {};
  for (let elemento in dic) {
    for (let item of dic[elemento]) {
      res[item.toLowerCase()] = Number(elemento);
    }
  }
  return res;
};
