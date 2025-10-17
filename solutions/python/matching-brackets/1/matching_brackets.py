def is_paired(cadena):
    stack = []
    pares = {'(': ')', '[': ']', '{': '}'}

    for caracter in cadena:
        if caracter in pares:
            stack.append(caracter)
        elif caracter in pares.values():
            if not stack or pares[stack.pop()] != caracter:
                return False

    return not stack

