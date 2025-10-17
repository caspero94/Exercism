class Queen:
    def __init__(self, row, column):
        if row < 0:
            raise ValueError("row not positive")
        elif row > 7:
            raise ValueError("row not on board")
        elif column < 0:
            raise ValueError("column not positive")
        elif column > 7:
            raise ValueError("column not on board")

        self.queen = [row,column]

    def can_attack(self, another_queen):
        
        if  self.queen == another_queen.queen:
            raise ValueError("Invalid queen position: both queens in the same square")
        x = -7
        for _ in range(15):
            if 8 > self.queen[0]+x > -1 and 8 > self.queen[1]+x > -1:
                if self.queen[0]+x == another_queen.queen[0] and self.queen[1]+x == another_queen.queen[1]:
                    return True
 
            
            if 8 > self.queen[0]+x > -1 and 8 > self.queen[1]-x > -1:
                if self.queen[0]+x == another_queen.queen[0] and self.queen[1]-x == another_queen.queen[1]:
                    return True
            x += 1
            
        if self.queen[0] == another_queen.queen[0] or self.queen[1] == another_queen.queen[1]:
            return True
        
        else:
            return False
