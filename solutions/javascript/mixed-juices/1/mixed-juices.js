export function timeToMixJuice(name) {
  switch (name){
    case "Pure Strawberry Joy":
      return 0.5
    case "Energizer":
    case "Green Garden":
      return 1.5
    case "Tropical Island":
      return 3
    case "All or Nothing":
      return 5
    default:
      return 2.5
  }
}

export function limeCut(lima){
  switch (lima){
    case 'small':
      return 6
    case 'medium':
      return 8
    case 'large':
      return 10
    }
}

export function limesToCut(wedgesNeeded, limes) {
  let rodajas = 0
  if (wedgesNeeded === 0){
    return 0
  }
  for (let i = 0; i < limes.length; i++) {
    rodajas += limeCut(limes[i])
    if (wedgesNeeded <= rodajas){
      return i+1
    }
  }
  return limes.length
}

export function remainingOrders(timeLeft, orders) {
  for (let i = 0; i < orders.length; i++){
    timeLeft -= timeToMixJuice(orders[i])
    if (timeLeft <= 1){
      return orders.slice(i+1)
    }
  }
}
