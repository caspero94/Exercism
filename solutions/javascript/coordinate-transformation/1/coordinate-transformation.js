export function translate2d(dx, dy) {
  return (p1,p2) => [dx+p1, dy+p2]
}

export function scale2d(sx, sy) {
  return (p1,p2) => [sx*p1, sy*p2]
}

export function composeTransform(f, g) {
  return (x, y) => g(...f(x,y))
}

export function memoizeTransform(f) {
  let cache = {}
  return (x,y) => cache.x === x && cache.y === y ? cache.result : (cache.x = x, cache.y = y, cache.result = f(x,y))
}
