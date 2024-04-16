import pandas as pd


def find_xth_largest(df, x, column, grouped_by):
    # Group the data by the given column and find the Xth largest value
    xth_largest = df.groupby(grouped_by)[column].nlargest(x).iloc[-1]


    return xth_largest


# Test the function
df = pd.DataFrame({'fruit': ['apple', 'banana', 'orange'] * 3,
                   'rating': [2,5,8,3,6,1,6,4,9],
                   'price': [1,2,3,4,5,6,7,8,9]})


x = 2
column = 'rating'
grouped_by = 'fruit'


result = find_xth_largest(df, x, column, grouped_by)


# Use assertions to validate the output
assert result == 8, f"Expected 6, but got {result}"


print("Assertion passed")