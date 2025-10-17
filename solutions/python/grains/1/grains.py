def square(number):
    if number > 64 or number < 1:
        raise ValueError("square must be between 1 and 64")
    x=1
    for i in range(0,number-1):
        x+=x
    return x


def total():
    return square(64)+square(64)-1
    
