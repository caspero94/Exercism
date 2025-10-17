def is_valid(isbn):
    isbn = isbn.replace(" ","").replace("-","")
    if len(isbn) == 10:
        control = isbn[9].replace("X","10")
        if control.isdigit() == True:
            isbn = isbn[0:9] 
            if isbn.isdigit() == True:
                e = 10
                check = 0
                for n in tuple(isbn):
                    check += int(n) * e
                    e -= 1
                check += int(control)
                if check%11 == 0:
                    return True
    return False