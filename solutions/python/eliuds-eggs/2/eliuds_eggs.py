def egg_count(n):
    res = 0
    while n > 0:
        res += n%2
        n //= 2
    return res
