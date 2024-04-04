import pandas as pd


# Create the DataFrame
df = pd.DataFrame([["A", 1], ["B", 2], ["C", 3], ["D", 4]],
                  columns=["Col_A", "Col_B"])


# Define the list for sorting
sort_list = ["C", "D", "B", "A"]


# Create a dictionary to map the values in the list to their order
sort_dict = {k: i for i, k in enumerate(sort_list)}


# Use the map function to replace the values in Col_A with their order
df['Col_A_temp'] = df['Col_A'].map(sort_dict)


# Sort the DataFrame by the temporary column
df.sort_values(by='Col_A_temp', inplace=True)


# Drop the temporary column
df.drop('Col_A_temp', axis=1, inplace=True)


print(df)