def is_pangram(sentence):
    abc = tuple("abcdefghijklmnopqrstuvwxyz")
    for letter in abc:
        if letter not in sentence.lower():
            return False
    return True
