def egg_count(n):
    res = 0
    if not n == 0:
         while n > 0:
            if not n % 2 == 0:
                res += 1
            n = n//2
    return res
