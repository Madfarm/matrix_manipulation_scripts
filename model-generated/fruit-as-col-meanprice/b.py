import pandas as pd


# Create the DataFrame
df = pd.DataFrame({'fruit': ['apple', 'banana', 'orange'] * 3,
                   'rating': [2,5,8,3,6,1,6,4,9],
                   'price': [1,2,3,4,5,6,7,8,9]})


# Group by fruit and calculate mean price
mean_prices = df.groupby('fruit')['price'].mean().reset_index()


# Rename the columns for clarity
mean_prices.columns = ['fruit', 'mean_price']


# Print the result
print(mean_prices)


# Use assertions to validate the output
assert mean_prices['fruit'].tolist() == ['apple', 'banana', 'orange']
assert mean_prices['mean_price'].tolist() == [4.0, 5.0, 6.0]