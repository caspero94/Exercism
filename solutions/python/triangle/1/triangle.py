def equilateral(sides):
    
    return sides[0] == sides[1] == sides[2] and check(sides)


def isosceles(sides):
    return (sides[0] == sides[1] or sides[1] == sides[2] or sides[2] == sides[0]) and check(sides) 


def scalene(sides):
    return isosceles(sides) == False and check(sides)


def check(sides):
    return sides[0] + sides[1] >= sides[2] and sides[1] + sides[2] >= sides[0] and sides[2] + sides[0] >= sides[1] and min(sides) > 0
    
        
    
