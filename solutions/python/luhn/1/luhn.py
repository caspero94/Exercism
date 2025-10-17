class Luhn:

    """
    Funcion Luhn.
    """

    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):

        """ 
        Validar si es un numero Luhn

        Returns:
            Bolean: Si es verdadero o falso
        """

        n = self.card_num.replace(" ","")

        if not n.isdigit() or n == "0":
            return False

        else:
            n =n[::-1]
            res = ""

            for p,d in enumerate(n):

                if p % 2 != 0:

                    if int(d) * 2 > 9:
                        res += str((int(d)*2)-9)

                    else:
                        res += str(int(d)*2)

                else:
                    res += d

            return sum(int(d) for d in res[::-1]) % 10 == 0

