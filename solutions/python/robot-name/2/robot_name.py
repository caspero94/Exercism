import random
import string


class Robot:
    def __init__(self):

        name = ''.join([random.choice(string.ascii_uppercase)
                       for _ in range(2)])
        name += ''.join([str(random.randint(0, 9)) for _ in range(3)])
        self.name = name

    def reset(self):
        self.name = self.name.replace("6", "0")

