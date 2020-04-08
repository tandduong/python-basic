import random


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second
        #return tuple from function does not need paranthesis


dice = Dice()
print(dice.roll())

