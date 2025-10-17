COLOR_VALUE ={"black":0,"brown":1,"red":2,"orange":3,"yellow":4,"green":5,"blue":6,"violet":7,"grey":8,"white":9}
TOLERANCE = {"grey":"±0.05%","violet":"±0.1%","blue":"±0.25%","green":"±0.5%","brown":"±1%","red":"±2%","gold":"±5%","silver":"±10%"}

def resistor_label(colors):  
    if len(colors) > 2:
        result =""
        multiplicador = int(COLOR_VALUE[colors[-2]])
        tolerance = TOLERANCE[colors[-1]]
        color = colors[:-2]

        for col in color:
            result += str(COLOR_VALUE[col])

        result += str(multiplicador*"0")
        if len(result)> 6:
            result = str(int(result)/1000000) + " megaohms "
        elif len(result)> 3:
            if int(result)%1000 == 0:
                result = str(int(int(result)/1000)) + " kiloohms "
            else:
                result = str(int(result)/1000) + " kiloohms "
        else:
            result += " ohms "
        
        return result + tolerance
    else:
        return "0 ohms"

"""    re = str(col[color[0]])+str(col[color[1]]) + col[color[2]]*"0"
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
    return re"""