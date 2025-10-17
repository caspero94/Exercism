def sum_of_multiples(limit, multiples):
    re = []
    for x in multiples:
        if x == 0:
            None
        else:
            n = 0
            p = x
            while p < limit:
                n += 1
                p = x*n
                if p < limit:
                    re.append(p)
    return sum(set(re))             
