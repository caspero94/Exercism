class PhoneNumber:
    def __init__(self, number):
        
        self.number = self.clean_number(number)
        self.area_code = self.number[0:3]

    def pretty(self):

        return "("+self.number[0:3]+")-"+self.number[3:6]+"-"+self.number[6:]
    
    def clean_number(self,number):
        puctuacion = ["@",":","!"]
        for n in number:
            if n.isalpha():
                raise ValueError("letters not permitted")
            if n in puctuacion:
                raise ValueError("punctuations not permitted")
        clean_number = ''.join(n for n in number if n.isdigit())
        if clean_number[0] == "0":
            raise ValueError("area code cannot start with zero")

        elif len(clean_number) < 10:
            raise ValueError("must not be fewer than 10 digits")
        elif len(clean_number) == 11:
            if clean_number[0] != "1":
                raise ValueError("11 digits must start with 1")
            if clean_number[1] == "0":
                raise ValueError("area code cannot start with zero")
            if clean_number[1] == "1":
                raise ValueError("area code cannot start with one")
            if clean_number[4] == "0":
                raise ValueError("exchange code cannot start with zero")
            if clean_number[4] == "1":
                raise ValueError("exchange code cannot start with one")
            return clean_number[1:]
        elif clean_number[0] == "1":
            raise ValueError("area code cannot start with one")
        elif clean_number[3] == "0":
            raise ValueError("exchange code cannot start with zero")
        
        elif clean_number[3] == "1":
            raise ValueError("exchange code cannot start with one")
        elif len(clean_number) > 11:
            raise ValueError("must not be greater than 11 digits")
        else:
            return clean_number

