# Globals for the directions
# Change the values as you see fit
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3



class Robot:
    def __init__(self, dir=NORTH, x=0, y=0):
        self.dir = dir
        self.x = x
        self.y = y

    def move(self, route):
        for x in route:
            if x == "A":
                if self.dir == 0:
                    self.y += 1
                elif self.dir == 1:
                    self.x += 1
                elif self.dir == 2:
                    self.y -= 1
                elif self.dir == 3:
                    self.x -= 1
            
            elif x == "R":
                self.dir = (self.dir + 1) % 4
            elif x == "L":
                self.dir = (self.dir - 1) % 4

    @property
    def coordinates(self):
        return (self.x, self.y)

    @property
    def direction(self):
        return self.dir
