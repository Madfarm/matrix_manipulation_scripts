import random


class Coin:
    def __init__(self, name, value, minting_date):
        self.name = name
        self.value = value
        self.minting_date = minting_date


    def flip_coin(self):
        if random.randint(0, 1) == 0:
            self.value *= 2
        else:
            self.value /= 2


# Create coins
quarter = Coin('quarter', 0.25, '12-1-1956')
silver_dollar = Coin('silver dollar', 13.34, '3-6-1833')


# Flip coins 3 times
for _ in range(3):
    quarter.flip_coin()
    silver_dollar.flip_coin()


# Print values
print(f'Quarter value: {quarter.value}')
print(f'Silver dollar value: {silver_dollar.value}')