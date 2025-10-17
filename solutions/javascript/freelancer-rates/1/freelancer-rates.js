export function dayRate(ratePerHour) {
  return ratePerHour * 8
}

export function daysInBudget(budget, ratePerHour) {
  return Math.floor(budget / dayRate(ratePerHour))
}

export function priceWithMonthlyDiscount(ratePerHour, numDays, discount) {
  return Math.ceil(((numDays % 22) * dayRate(ratePerHour)) + ((numDays - (numDays % 22))* dayRate(ratePerHour) - (discount * (numDays - (numDays % 22))* dayRate(ratePerHour))))
}
