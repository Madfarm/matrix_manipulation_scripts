import pandas as pd


# Create a DataFrame
df = pd.DataFrame({'fruit': ['apple', 'banana', 'orange'] * 3,
                   'rating': [2,5,8,3,6,1,6,4,9],
                   'price': [1,2,3,4,5,6,7,8,9]})


# Group by fruit and calculate the mean price
mean_prices = df.groupby('fruit')['price'].mean().reset_index()


# Rename the columns for clarity
mean_prices.columns = ['fruit', 'mean_price']


# Use assertions to validate the output
assert mean_prices.loc[0, 'fruit'] == 'apple'
assert mean_prices.loc[1, 'fruit'] == 'banana'
assert mean_prices.loc[2, 'fruit'] == 'orange'


assert mean_prices.loc[0, 'mean_price'] == 4.0
assert mean_prices.loc[1, 'mean_price'] == 5.0
assert mean_prices.loc[2, 'mean_price'] == 6.0