
export function pizzaPrice(pizza, ...extras) {
  const base = pizza === "Margherita" ? 7 : pizza === "Caprese" ? 9 : 10
  if (!extras.length) return base
  const [extra, ...rest] = extras
  const cost = extra === "ExtraSauce" ? 1 : 2
  return cost + pizzaPrice(pizza, ...rest)
}

export function orderPrice(pizzaOrders) {
  let total = 0
  if (!pizzaOrders.length) return 0
  for (let order of pizzaOrders){
    total += pizzaPrice(order.pizza, ...order.extras)
  }
  return total
}
