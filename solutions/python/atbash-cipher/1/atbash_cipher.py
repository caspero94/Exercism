plain = list("abcdefghijklmnopqrstuvwxyz")
cipher = list("zyxwvutsrqponmlkjihgfedcba")

def encode(plain_text):
    text = plain_text.replace(" ","").replace(",","").replace(".","").lower()
    new_text = ""
    x = -1
    for t in text:
        x += 1
        if x%5 == 0:
            new_text += " "
        if t.isnumeric():
            new_text += t
        else:
            new_text += (cipher[plain.index(t)])
    return new_text[1:]

def decode(ciphered_text):
    text = ciphered_text.replace(" ","").replace(",","").replace(".","").lower()
    new_text = ""
    for t in text:
        if t.isnumeric():
            new_text += t
        else:
            new_text += (plain[cipher.index(t)])
    return new_text
