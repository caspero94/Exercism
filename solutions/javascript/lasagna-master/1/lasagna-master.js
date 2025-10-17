export function cookingStatus(minutes) {
  return minutes > 0 ? 'Not done, please wait.' : minutes === 0 ? 'Lasagna is done.' : 'You forgot to set the timer.' 
}

export function preparationTime(layers, avgMinute = 2) {
  return  layers.length * avgMinute
}

export function quantities(listIng) {
  const res = { noodles: 0, sauce: 0 };
  listIng.forEach(i => i === 'noodles' ? res.noodles += 50 : i === 'sauce' ? res.sauce += 0.2 : null);
  return res;
}


export function addSecretIngredient(friendsList, myList) {
  myList.push(friendsList.at(-1))
}

export function scaleRecipe(recipe, portions) {
  const recipe2 = {...recipe}
  for (let clave in recipe2){
    recipe2[clave] = (recipe2[clave]/2)* portions
  }
  return recipe2
}