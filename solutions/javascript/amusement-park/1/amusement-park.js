
export function createVisitor(name, age, ticketId) {
  return {'name': name,'age': age,'ticketId': ticketId}
}

export function revokeTicket(visitor) {
  return (visitor.ticketId = null, visitor)
}

export function ticketStatus(tickets, ticketId) {
  return tickets[ticketId] === null ? "not sold" : tickets[ticketId] === undefined ? "unknown ticket id" : "sold to " + tickets[ticketId]
}
export function simpleTicketStatus(tickets, ticketId) {
  return tickets[ticketId] ?? 'invalid ticket !!!'
}

export function gtcVersion(visitor) {
  return visitor?.gtc?.version
}
