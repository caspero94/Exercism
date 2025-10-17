def factors(value):
    result = []
    x = 2
    while value > 1:
        if value % x== 0:
            value = value/x
            result.append(x)
        else:
            x +=1
    return result
