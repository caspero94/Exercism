def triplets_with_sum(number):
    lista = []
    for c in range(number//3,number):
        for a in range(1,(number-c)-(c//2)):
            b = number-a-c
            if a < b < c and (a**2 + b**2 == c**2):
                lista.append([a,b,c])
    return lista