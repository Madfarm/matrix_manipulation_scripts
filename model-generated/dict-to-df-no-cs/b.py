import pandas as pd


data = {'name': ['Ash', 'Jack', 'Bob'], 'college': ['Westover', 'State', 'Community'], 'city': ['Welltown', 'Spittsberg', 'Lenty'], 'age': [22,34,23] }


# Create a DataFrame
df = pd.DataFrame(data)


# Filter out columns that start with 'c'
df = df.loc[:, ~df.columns.str.startswith('c')]


print(df)