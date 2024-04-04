import pandas as pd


# Create the initial DataFrame
df = pd.DataFrame([["A", 1], ["B", 2], ["C", 3], ["D", 4]], 
                  columns=["col_A", "col_B"])


# Define the row to be inserted
insert_row = ["P", 5]


# Specify the index at which the row should be inserted
insert_index = 2


# Insert the row at the specified index
df.loc[insert_index] = insert_row


# Reassign the indexes
df.index = range(df.shape[0])


# Print the updated DataFrame
print(df)