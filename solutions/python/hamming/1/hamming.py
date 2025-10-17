def distance(a, b):
    count = 0
    if len(a) == len (b):
        for x in range(len(a)):
            if a[x] != b[x]:
                count += 1
        return count
    else:
        raise ValueError("Strands must be of equal length.")