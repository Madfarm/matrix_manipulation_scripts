import pandas as pd

# Sample DataFrame
df = pd.DataFrame({'A': [1, 2, 3, 2], 'B': [4, 5, 6, 2]})

print(df)
# Find indices of a particular value in column 'A'
value = 2
indices = df.index[df['A'] == value].tolist()

print(indices)