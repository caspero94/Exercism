def is_armstrong_number(number):
    e = 0
    if (len(str(number))) == 1:
            return True
    for num in tuple(str(number)):      
        if int(num) == 1:
            e += 1
        else:
            e += int(num) ** (len(tuple(str(number))))
    print(e,num)
    return e == number
