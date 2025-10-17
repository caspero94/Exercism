def convert(input_grid):
    if len(input_grid[0]) % 3:
        raise ValueError("Number of input columns is not a multiple of three")
    if len(input_grid) % 4:
        raise ValueError("Number of input lines is not a multiple of four")
    r = ""
    for j in range(0, len(input_grid)//4):
        if j > 0:
            r += ","
        for x in range(0, (len(input_grid[0])//3)):

            e = (x+1)*3
            y = x*3
            letter = [input_grid[j*4][y:e], input_grid[j*4+1][y:e],
                      input_grid[j*4+2][y:e], input_grid[j*4+3][y:e]]
            if letter == [" _ ", "| |", "|_|", "   "]:
                r += "0"
            elif letter == ['   ', '  |', '  |', '   ']:
                r += "1"
            elif letter == [' _ ', ' _|', '|_ ', '   ']:
                r += "2"
            elif letter == [' _ ', ' _|', ' _|', '   ']:
                r += "3"
            elif letter == ['   ', '|_|', '  |', '   ']:
                r += "4"
            elif letter == [' _ ', '|_ ', ' _|', '   ']:
                r += "5"
            elif letter == [' _ ', '|_ ', '|_|', '   ']:
                r += "6"
            elif letter == [' _ ', '  |', '  |', '   ']:
                r += "7"
            elif letter == [' _ ', '|_|', '|_|', '   ']:
                r += "8"
            elif letter == [' _ ', '|_|', ' _|', '   ']:
                r += "9"
            else:
                r += "?"

            letter = []
    return r
    