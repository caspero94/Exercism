export function twoSum(array1, array2) {
  return Number(array1.join('')) + Number(array2.join(''))
}

export function luckyNumber(value) {
  return String(value) === [...String(value)].reverse().join('')
  
}

export function errorMessage(input) {
  return input == null || input === "" ? 'Required field' : Number(input) ? '' : 'Must be a number besides 0'
}
