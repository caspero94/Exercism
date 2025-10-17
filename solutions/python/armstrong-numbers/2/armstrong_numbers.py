def is_armstrong_number(n):
    s = str(n)
    size = len(s)
    return n == sum(int(c) ** size for c in s)
