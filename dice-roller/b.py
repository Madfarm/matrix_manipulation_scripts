import random

class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

    def roll_yahtzee(self):
        return [random.randint(1, self.sides) for _ in range(5)]

    def roll_farkle(self):
        rolls = [random.randint(1, self.sides) for _ in range(6)]
        if 1 in rolls:
            return "Farkle!"
        else:
            return rolls

# Create a 6-sided die
dice = Dice()

# Roll the die
print(dice.roll())

# Roll 5 dice for Yahtzee
print(dice.roll_yahtzee())

# Roll 6 dice for Farkle
print(dice.roll_farkle())

