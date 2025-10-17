/**
 * for (let i = 0; i< number.length; i++){}
 * for (const item of arrayItems){}
 * arrayItems.forEach((number,index)=> {})
 */

export function cardTypeCheck(stack, card) {
  // 🚨 Use .forEach
  let count = 0
  stack.forEach((number, index)=>{
    count = number === card ? count+1 : count
  })
  return count
}

export function determineOddEvenCards(stack, type) {
  // 🚨 Use a `for...of` loop
  let count = 0
  for (const card of stack) if ((card % 2 === 0)=== type) count++
  return count
}
