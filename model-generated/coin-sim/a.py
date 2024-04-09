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


# Create a DataFrame to store the results
df = pd.DataFrame(columns=['quarter', 'silver_dollar', 'avg_value'])


# Flip coins 3 times each
for i in range(3):
    quarter.flip_coin()
    silver_dollar.flip_coin()


    # Append the values to the DataFrame
    df.loc[i] = [quarter.value, silver_dollar.value, None]


# Calculate the average value for each coin
df.loc[3] = [df['quarter'].mean(), df['silver_dollar'].mean(), None]


# Print the DataFrame
print(df)