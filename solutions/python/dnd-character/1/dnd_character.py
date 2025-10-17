class Character:
    def __init__(self):
        self.strength = Character.dados()
        self.dexterity = Character.dados()
        self.constitution = Character.dados()
        self.intelligence = Character.dados()
        self.wisdom = Character.dados()
        self.charisma = Character.dados()
        self.hitpoints = 10 + modifier(self.constitution)
    def dados():
        import random
        dados = []
        for _ in range(4):
            dados.append(random.randint(1,2))
        del dados[dados.index(min(dados))]
        return sum(dados)
    def ability(self):
        return self.constitution

def modifier(n):
    return (n - 10) // 2
