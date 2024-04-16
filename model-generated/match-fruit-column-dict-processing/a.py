import pandas as pd


def find_matches(df, col1, col2):
    # Ensure the columns exist in the data frame
    assert col1 in df.columns and col2 in df.columns, "Both columns must exist in the data frame"


    # Find the positions where the two columns match
    matches = df[col1] == df[col2]


    # Count the number of matching values
    count = matches.sum()


    # Create a dictionary to store the results
    result = {'positions': df.index[matches].tolist(), 'count': count}


    return result


# Test the function
df = pd.DataFrame({'fruit1': ['apple', 'orange', 'banana', 'apple', 'orange', 'banana', 'banana', 'orange', 'apple', 'orange'],
                    'fruit2': ['apple', 'apple', 'banana', 'orange', 'banana', 'banana', 'apple', 'orange', 'apple', 'banana']
})


result = find_matches(df, 'fruit1', 'fruit2')

assert result == {'positions': [0, 2, 5, 7, 8], 'count': 5}