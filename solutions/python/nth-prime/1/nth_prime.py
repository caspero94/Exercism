def prime(n):
    if n < 1:
        raise ValueError('there is no zeroth prime')
    res = []
    number = 1
    while len(res) < n:
        number +=1
        if check_prime(number) == True:
            res.append(number)
    return int(res[-1])
        
    

def check_prime(n):
    for x in range(2, int(n ** 0.5) + 1):
        if n%x == 0:
            return False
    return True