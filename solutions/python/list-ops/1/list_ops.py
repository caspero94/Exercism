def append(list1, list2):
    for n in list2:
        list1.append(n)
    return list1

def concat(lists):
    res = []
    for n in lists:
        for nn in n:
            res.append(nn)
    return res
        

def filter(function, list):
    res = []
    for x in list:
        if function(x):
            res.append(x)
    return res


def length(list):
    x = 0
    for _ in list:
        x += 1
    return x


def map(function, list):
    res = []
    for n in list:
        res.append(function(n))
    return res

def foldl(function, list, initial):
    for n in list:
        initial = function(initial,n)
    return initial


def foldr(function, list, initial):
    for n in reverse(list):
        initial = function(initial,n)
    return initial


def reverse(list):
    return list[::-1]
