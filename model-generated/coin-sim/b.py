import random
import pandas as pd


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


# Create a dictionary to store the coin values
coin_values = {'quarter': [], 'silver dollar': []}


# Flip coins 3 times each
for i in range(3):
    quarter.flip_coin()
    silver_dollar.flip_coin()


    coin_values['quarter'].append(quarter.value)
    coin_values['silver dollar'].append(silver_dollar.value)


# Create a DataFrame
df = pd.DataFrame(coin_values)


# Calculate the average value for each coin
df['avg_value'] = df.mean(axis=1)


print(df)