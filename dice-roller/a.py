import random

class Dice:
    def __init__(self):
        pass

    def roll_dice(self, sides):
        return random.randint(1, sides)

    def roll_multiple_dice(self, num_dice, sides):
        return [self.roll_dice(sides) for _ in range(num_dice)]

    def roll_yahtzee(self):
        return self.roll_multiple_dice(5, 6)

    def roll_dnd(self):
        return self.roll_multiple_dice(4, 6)

dice = Dice()
print(dice.roll_dice(20))  # roll a single 20-sided die
print(dice.roll_multiple_dice(2, 20))  # roll 2 20-sided dice
print(dice.roll_yahtzee())  # roll 5 6-sided dice (Yahtzee)
print(dice.roll_dnd())  # roll 4 6-sided dice (Dungeons & Dragons)