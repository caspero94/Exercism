def steps(n):
    if n < 1:
        raise ValueError("Only positive integers are allowed")
    s = 0
    while n != 1:
        s += 1
        n = int(n/2 if n % 2 == 0 else n*3+1)
    return s
