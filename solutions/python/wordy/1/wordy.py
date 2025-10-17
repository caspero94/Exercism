def answer(question):
    operation = ["plus","minus","multiplied","divided"]
    words = question.replace("?","").replace("by","").split()
    if words[0:2] != ["What","is"] or "cubed" in words:
        raise ValueError("unknown operation")
    if len(words)<3 or words[2].isalpha():
        raise ValueError("syntax error")
    res = int(words[2])
    words = words[3:]
    while len(words)>0:
        try:
            if words[0] == "plus":
                res += int(words[1])
            elif words[0] == "minus":
                res -= int(words[1])
            elif words[0] == "multiplied":
                res *= int(words[1])
            elif words[0] == "divided":
                res //= int(words[1])
            else:
                raise ValueError("syntax error")
            words = words[2:]
        except:
            raise ValueError("syntax error")
    return res