def commands(binary):
    secret = []
    if binary[4] == "1":
        secret += ["wink"]
    if binary[3] == "1":
        secret += ["double blink"]
    if binary[2] == "1":
        secret += ["close your eyes"]
    if binary[1] == "1":
        secret += ["jump"]
    if binary[0] == "1":
        secret.reverse()
    return secret
