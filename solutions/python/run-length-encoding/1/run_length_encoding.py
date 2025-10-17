def decode(string):
    res = ""
    for posicion,letra in enumerate(string):
        if letra.isnumeric():
            if string[posicion+1].isnumeric(): 
                res += ((int(string[posicion])*10)*(string[posicion+2])) 
            else:
                res += (int(letra)-1)*string[posicion+1]
                
        else:
            res += letra
    return res
def encode(string):
    cant = 1
    res = ""
    for posicion,letra in enumerate(string):
        if posicion < len(string)-1 and letra == string[posicion+1]:
            cant +=1
        else:
            if cant > 1:
                res += str(cant)
                cant = 1
            res +=letra

    return res
