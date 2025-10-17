ALLERGIES = {128:"cats", 64:"pollen", 32:"chocolate", 16:"tomatoes", 8:"strawberries", 4:"shellfish", 2:"peanuts", 1:"eggs"}

class Allergies:

    def __init__(self, score):
        self.list_allergies = []
        next = 256
        while score > 255:
            score -= next
            next *= 2
            
        while score > 0:
            for sco in ALLERGIES:
                if score >= sco:
                    self.list_allergies.insert(0,ALLERGIES[sco])
                    score -= sco

    def allergic_to(self, item):
        if item in self.list_allergies:
            return True
        else:
            return False

    @property
    def lst(self):
        return self.list_allergies
