
export function randomShipRegistryNumber() {
  return `NCC-${Math.floor(Math.random()*8999)+1002}`
}

export function randomStardate() {
  return (Math.random()*10)+41000
}

export function randomPlanetClass() {
  const planetClasses = ["D", "H", "J", "K", "L", "M", "N", "R", "T", "Y"];
  return planetClasses[Math.floor(Math.random()*planetClasses.length)]
}
