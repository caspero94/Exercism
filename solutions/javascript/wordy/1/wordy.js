export const answer = (operation) => {
  if (!operation.startsWith("What is") || !operation.endsWith("?")) {
    throw new Error("Unknown operation");
  }
  const opArray = operation
    .replace("?", "")
    .replace("What is ", "")
    .replaceAll("by ", "")
    .split(" ");

  if (opArray.length === 0) throw new Error("Syntax error");

  let acc = Number(opArray[0]);

  for (let i = 1; i < opArray.length; i++) {
    if (!isNaN(opArray[i]) && !isNaN(opArray[i - 1]))
      throw new Error("Syntax error");
    if (isNaN(opArray[i]) && isNaN(opArray[i - 1]))
      throw new Error("Syntax error");

    if (isNaN(opArray[i])) {
      if (!["plus", "minus", "multiplied", "divided"].includes(opArray[1])) {
        throw new Error("Unknown operation");
      }

      if (i + 1 >= opArray.length || isNaN(opArray[i + 1])) {
        throw new Error("Syntax error");
      }

      if (opArray[i] === "plus") acc += Number(opArray[i + 1]);
      else if (opArray[i] === "minus") acc -= Number(opArray[i + 1]);
      else if (opArray[i] === "multiplied") acc *= Number(opArray[i + 1]);
      else if (opArray[i] === "divided") acc /= Number(opArray[i + 1]);
    }
  }

  return acc;
};
