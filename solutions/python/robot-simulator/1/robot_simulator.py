# Globals for the directions
# Change the values as you see fit
NORTH = 1
EAST = 2
SOUTH = 3
WEST = 4



class Robot:
    def __init__(self, dir=NORTH, x=0, y=0):
        self.dir = dir
        self.x = x
        self.y = y

    def move(self, route):
        for x in route:
            if x == "A":
                if self.dir == 1:
                    self.y += 1
                elif self.dir == 2:
                    self.x += 1
                elif self.dir == 3:
                    self.y -= 1
                elif self.dir == 4:
                    self.x -= 1
            
            elif x == "R":
                if self.dir == 4:
                    self.dir = 1
                else:
                    self.dir += 1
            elif x == "L":
                if self.dir == 1:
                    self.dir = 4
                else:
                    self.dir -= 1

    @property
    def coordinates(self):
        return (self.x, self.y)

    @property
    def direction(self):
        return self.dir
