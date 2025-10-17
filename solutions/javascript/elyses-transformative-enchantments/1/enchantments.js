export function seeingDouble(deck) {
  const newDeck = deck.map((value) => value*2)
  return newDeck
}

export function threeOfEachThree(deck) {
  return deck.reduce((acc, value) => {
    if (value === 3) {
      // Si el valor es 3, agregamos tres veces el número 3
      return [...acc, 3, 3, 3];
    } else {
      return [...acc, value];
    }
  }, []);
}

export function middleTwo(deck) {
  return deck.slice(4,6)
}



export function sandwichTrick(deck) {
  const fc= deck.splice(0,1)
  const lf= deck.splice(deck.length -1, 1)
  deck.splice(deck.length/2, 0, lf[0], fc[0])
  return deck
  
}


export function twoIsSpecial(deck) {
  return deck.filter((value)=> value === 2)
}

export function perfectlyOrdered(deck) {
  return deck.sort((a,b)=> a - b)
}


export function reorder(deck) {
  return deck.reverse()
}
