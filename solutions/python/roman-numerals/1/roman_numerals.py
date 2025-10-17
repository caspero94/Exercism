def roman(number):
    n = str(number)
    l = len(n)
    res = ""
    for x in n:
        l -=1
        e = x+(l*"0")
        if int(e) >= 1000:
            res += ("M"* int(e[0]))
        elif int(e) == 900:
            res += "CM"    
        elif int(e) >=500:
            res += "D" + ((int(e[0])-5)*"C")
        elif int(e) == 400:
            res += "CD"    
        elif int(e) >90:
            res += ("C"* int(e[0]))
        elif int(e)==90:
            res += "XC"
        elif int(e)>=50:
            res += "L" + ((int(e[0])-5)*"X")
        elif int(e)== 40:
            res += ("XL")
        elif int(e) >9:
            res += ("X"* int(e[0]))
        elif int(e) == 9:
            res += "IX"
        elif int(e) >=5:
            res += "V" + ((int(e)-5)*"I")
        elif int(e)== 4:
            res+= ("IV")
        elif int(e) <4:
            res += ("I"* int(e[0]))
        print(e)
    return res