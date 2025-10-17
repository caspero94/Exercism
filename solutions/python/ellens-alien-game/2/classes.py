"""Solution to Ellen's Alien Game exercise."""

class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """
    total_aliens_created = 0
    def __init__(self, x_c,y_c):
        self.x_coordinate = x_c
        self.y_coordinate = y_c
        self.health = 3
        Alien.total_aliens_created += 1            
    def hit(self):
        self.health -= 1
    def is_alive(self):
        return False if self.health < 1 else True
    def teleport(self,x_c,y_c):
        self.x_coordinate += x_c
        self.y_coordinate += y_c
    def collision_detection(self,other):
        pass
            
#TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.
def new_aliens_collection(coordinates_list):
    aliens = []
    for x_c, y_c in coordinates_list:
        new_alien = Alien(x_c, y_c)
        aliens.append(new_alien)
    return aliens
