col ={"black":0,"brown":1,"red":2,"orange":3,"yellow":4,"green":5,"blue":6,"violet":7,"grey":8,"white":9}
def label(color):
    re = str(col[color[0]])+str(col[color[1]]) + col[color[2]]*"0"
    re.lstrip('0')
    print(re)
    if "000000000" == re[-9:]:
        re = re[:-9]+" gigaohms"
    elif "000000" == re[-6:]:
        re = re[:-6]+" megaohms"
    elif "000" == re[-3:]:
        re = re[:-3]+" kiloohms"
    else:
        re = re + " ohms"
    if re == "00 ohms":
        re = "0 ohms"
    if re != "0 ohms":
        re = re.lstrip('0')
    return re