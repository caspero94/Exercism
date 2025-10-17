def response(hey_bob):
    caracteres_a_eliminar = [" ", "\t", "\n", "\r"]
    for caracter in caracteres_a_eliminar:
        hey_bob = hey_bob.replace(caracter, "")
    if hey_bob =="":
        return "Fine. Be that way!"
    if tuple(hey_bob[-1]) == ("?",) and hey_bob.isupper():
        return "Calm down, I know what I'm doing!"
    elif hey_bob.isupper():
        return "Whoa, chill out!"
    elif tuple(hey_bob[-1]) == ("?",):
        return "Sure."
    
    else:
        return "Whatever."