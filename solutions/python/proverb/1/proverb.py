def proverb(*data, qualifier):
    res = []
    for n in range(len(data),0,-1):
        if n == 1:
            if qualifier == None:
                qualifier = ""
            else:
                qualifier += " " 
            res.append(f"And all for the want of a {qualifier}{data[n-1]}.")
        elif n > 1:
            res.insert(0,(f"For want of a {data[(n-2)]} the {data[(n-1)]} was lost."))
    return res