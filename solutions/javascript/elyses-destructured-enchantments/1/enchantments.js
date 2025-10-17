
export function getFirstCard(deck) {
  const [a] = deck
  return a
}

export function getSecondCard(deck) {
  const [a,b] = deck
  return b
}

export function swapTwoCards(deck) {
  const [a,b] = deck
  return [b,a]
 }

export function shiftThreeCardsAround(deck) {
  const [a,b,c] = deck
  return [b,c,a]
}

export function pickNamedPile(piles) {
  const {chosen:chosen} = piles
  return chosen
}

export function swapNamedPile(piles) {
  // 🪄 Don't break the magic.
  // 🚨 Do NOT use piles.chosen or piles.disregarded.
  // 🚨 Do NOT touch the next line or Elyse will accidentally reveal the trick.
  const {chosen:disregarded, disregarded:chosen} = piles
  return { chosen, disregarded };
}
