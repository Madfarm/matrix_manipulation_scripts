import pandas as pd
import numpy as np


# Create a DataFrame
df = pd.DataFrame([["A", 1], ["B", 2], ["C", 3], ["D", 4]], 
                  columns=["col_A", "col_B"])


# Function to split the DataFrame into equal parts
def split_dataframe(df, n):
    # Calculate the number of rows in each part
    rows_per_part = len(df) // n


    # Split the DataFrame into parts
    parts = [df[i:i+rows_per_part] for i in range(0, len(df), rows_per_part)]


    return parts


# Split the DataFrame into 2 parts
parts = split_dataframe(df, 2)


# Print the parts
for i, part in enumerate(parts):
    print(f"Part {i+1}:")
    print(part)
    print()


