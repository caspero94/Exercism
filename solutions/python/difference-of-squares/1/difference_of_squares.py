def square_of_sum(n):
    e = 0
    for x in range(1,n+1):
        e += x
    return e*e


def sum_of_squares(n):
    e = 0
    for x in range(1,n+1):
        e += x*x
    return e


def difference_of_squares(n):
    return square_of_sum(n)-sum_of_squares(n)
