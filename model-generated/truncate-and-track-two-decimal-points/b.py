import pandas as pd
import numpy as np


# Create the data frame
df = pd.DataFrame({'Name': ['Seth', 'Eshanta', 'Jiametryc', 'Ash', 'Wallu'],
                   'GPA': [2.43333222, 3.812, np.nan, np.nan, 2.156545], 
                   'Age': [30.6417, 56.13423, 81.3434, np.nan, 21.5673],
                   'Salary': [np.nan, 80000.2363, 41000.454, 33000.4523, 20900.4587],
                })


def truncate_values(df):
    # Initialize a list to store lost values for each row
    lost_values_list = []


    # Iterate over each row in the dataframe
    for index, row in df.iterrows():
        # Initialize a variable to keep track of total lost value per row
        lost_value_row = 0


        # Iterate over each column except Name (assuming it's not numeric)
        for col_name in ['GPA', 'Age', 'Salary']:
            if not pd.isna(row[col_name]):
                original_val = row[col_name]
                truncated_val = round(original_val, 2) # Truncate down to two decimal points


                lost_value_cell = abs(truncated_val - original_val) # Calculate how much was lost from truncation
                lost_value_row += lost_value_cell # Add this amount to the running total for the current row


                df.loc[index, col_name] = truncated_val # Replace the cell with its truncated version


        lost_values_list.append(lost_value_row) # Append the total lost value for the current row


    df['Lost_Values'] = lost_values_list # Add new Lost Values column to dataframe


    return df


# Test the function using assertions
assert truncate_values(df).equals(pd.DataFrame({
   'Name': ['Seth', 'Eshanta', 'Jiametryc', 'Ash', 'Wallu'], 
   'GPA': [2.43, 3.81, np.nan, np.nan, 2.16], 
   'Age': [30.64, 56.13, 81.34, np.nan, 21.57], 
   'Salary': [np.nan, 80000.24, 41000.45, 33000.45, 20900.46], 
   'Lost_Values': [1.999998e-06 + 6.17e-05, 8.63e-04 + 9.000000000003448e-07 + 0.001363, 5.96e-03, 0.0024523, 8.700000000006297e-08]}))


print("All tests passed.")