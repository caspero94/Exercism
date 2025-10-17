abc = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
def rows(letter):
    space = abc.index(letter)
    in_sp = 0
    res = []

    if letter == "A":
        return ["A"]
    if letter == "B":
        return [" A ", "B B", " A "]
    else:
        for x in abc[:abc.index(letter)+1]:
            if in_sp == 0:
                res.append(space*" "+x+space*" ")
                in_sp += 1
            else:
                res.append(space*" "+x+in_sp*" "+x+space*" ")
                in_sp = in_sp+2
            space -= 1
        for x in abc[abc.index(letter)-1::-1]:
            if x == abc[abc.index(letter)-1]:
                in_sp -= 4
                space += 2
                res.append(space*" "+x+in_sp*" "+x+space*" ")
            elif x == "A":
                res.append(space*" "+x+space*" ")    
            else:
                in_sp = in_sp-2
                res.append(space*" "+x+in_sp*" "+x+space*" ")
            
            space += 1
    return res