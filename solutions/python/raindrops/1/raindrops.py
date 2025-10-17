def convert(nu):
    n = ""
    if nu % 3 == 0:
        n += "Pling"
    if nu % 5 == 0:
        n += "Plang"
    if nu % 7 == 0:
        n += "Plong"
    if n == "":
        n = str(nu)
    return n
