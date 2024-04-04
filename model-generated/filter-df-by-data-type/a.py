import pandas as pd


# Create a DataFrame
df = pd.DataFrame([["A", 1, True], ["B", 2, False],
                   ["C", 3, False], ["D", 4, True]], 
                  columns=["col_A", "col_B", "col_C"])


# Define the data type
dt_type = "bool"


# Filter columns based on the data type
filtered_df = df.select_dtypes(include=[dt_type])


print(filtered_df)