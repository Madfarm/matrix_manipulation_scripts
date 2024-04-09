import random


class Coin:
    def __init__(self, name, value, minting_date):
        self.name = name
        self.value = value
        self.minting_date = minting_date


    def flip_coin(self):
        if random.random() < 0.5:
            self.value *= 2
        else:
            self.value /= 2


# Create coins
quarter = Coin('quarter', 0.25, '12-1-1956')
silver_dollar = Coin('silver dollar', 13.34, '3-6-1833')


# Flip coins 3 times each
for i in range(3):
    quarter.flip_coin()
    silver_dollar.flip_coin()


    print(f'Quarter value after flip {i+1}: {quarter.value}')
    print(f'Silver dollar value after flip {i+1}: {silver_dollar.value}')