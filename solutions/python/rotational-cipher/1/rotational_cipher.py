def rotate(text, key):
    abc = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for letter in text:
        if letter.isalpha():
            ind = (abc.index(letter.lower())+key)%26
            result += abc[ind].upper() if letter.isupper() else abc[ind]
        else:
            result += letter
    return result