import pandas as pd


# Create a dictionary
data = {'name': ['Ash', 'Jack', 'Bob'], 
        'college': ['Westover', 'State', 'Community'], 
        'city': ['Welltown', 'Spittsberg', 'Lenty'], 
        'age': [22,34,23]}


# Filter out keys that start with 'c'
filtered_data = {key: value for key, value in data.items() if not key.startswith('c')}


# Create a DataFrame
df = pd.DataFrame(filtered_data)


print(df)