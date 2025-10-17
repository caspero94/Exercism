# Score categories.
# Change the values as you see fit.
YACHT = 50
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
    if category == YACHT and (dice[0] == dice[1] == dice[2] == dice[3] == dice [4]):
        return category
    if category == CHOICE:
        return sum(dice)
    dice.sort()
    if category == FULL_HOUSE and ((dice[0] == dice[1] == dice[2] != dice[3] == dice [4]) or (dice[0] == dice[1] != dice[2] == dice[3] == dice [4])):
        return sum(dice)
    if category == FOUR_OF_A_KIND and (dice[0] == dice[1] == dice[2] == dice[3]):
        return sum(dice[:4])
    if category == FOUR_OF_A_KIND and (dice[1] == dice[2] == dice[3] == dice [4]):
        return sum(dice[1:])
    if (category == LITTLE_STRAIGHT and (dice == [1,2,3,4,5])) or (category == BIG_STRAIGHT and (dice == [2,3,4,5,6])):
        return 30
    
    res = 0
    for x in dice:
        if category == x:
            res += category
    return res
