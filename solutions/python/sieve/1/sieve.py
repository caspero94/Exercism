def primes(limit):
    primes = [x for x in range(2,limit+1)]
    for n in primes:
        for i in range(2,limit+1):
            print(f"n = {n} i = {i} total {n*i}")
            if n*i > limit:
                break
            try:
                primes.remove((n*i))
            except:
                pass
    return primes