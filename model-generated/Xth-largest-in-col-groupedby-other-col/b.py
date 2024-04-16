import pandas as pd


# Create the DataFrame
df = pd.DataFrame({'fruit': ['apple', 'banana', 'orange'] * 3,
                   'rating': [2,5,8,3,6,1,6,4,9],
                   'price': [1,2,3,4,5,6,7,8,9]})


def find_xth_largest(df, x, column, grouped_by):
    # Group the data by the 'fruit' column and find the Xth largest value of 'rating'
    xth_largest = df[df['fruit'] == grouped_by][column].nlargest(x).iloc[-1]


    return xth_largest


# Test the function with assertions
x = 2
column = 'rating'
grouped_by = 'banana'


result = find_xth_largest(df, x, column, grouped_by)


assert result == 5, f"Expected the {x}th largest '{column}' for '{grouped_by}' to be 5, but got {result}"