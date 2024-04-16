import pandas as pd


def find_matching_values(df, col1, col2):
    assert col1 in df.columns and col2 in df.columns, "Columns not found in the data frame"


    matching_positions = df[df[col1] == df[col2]].index.tolist()
    num_matching_values = len(matching_positions)


    return {"matching_positions": matching_positions, "num_matching_values": num_matching_values}


# Test the function
df = pd.DataFrame({'fruit1': ['apple', 'orange', 'banana', 'apple', 'orange', 'banana', 'banana', 'orange', 'apple', 'orange'],
                   'fruit2': ['apple', 'apple', 'banana', 'orange', 'banana', 'banana', 'apple', 'orange', 'apple', 'banana']})


result = find_matching_values(df, 'fruit1', 'fruit2')
print(result)