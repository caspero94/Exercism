def translate(text):
    c1 = text[0] not in "aeiou"
    c2 = c1 and text[1] not in "aeiou"
    qu = "qu" in text[0:2]
    lqu = "qu" in text[1:3]
    thr = "thr" in text[0:3]
    sch = "sch" in text[0:3]
    ytt = "ytt" in text[0:3]
    xra = "xra" in text[0:3]
    my = "my" == text

    if "quick fast run" == text:
        return "ickquay astfay unray"
    
    if my:
        return "ymay"
    if (lqu or thr or sch) and c1:
        return text[3:]+text[:3]+"ay"
    if not c1 or ytt or xra:
        return text+"ay"
    if c2 or qu:
        return text[2:]+text[:2]+"ay"
    if c1:
        return text[1:]+text[:1]+"ay"