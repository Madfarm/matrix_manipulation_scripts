import pandas as pd


# Create a DataFrame
df = pd.DataFrame([["A", 1], ["B", 2], ["C", 3], ["D", 4]],
                  columns = ["Col_A", "Col_B"])


# Define the sort list
sort_list = ["C", "D", "B", "A"]


# Sort the DataFrame
df_sorted = df.loc[df['Col_A'].apply(lambda x: sort_list.index(x)).sort_values().index]


# Print the sorted DataFrame
print(df_sorted)