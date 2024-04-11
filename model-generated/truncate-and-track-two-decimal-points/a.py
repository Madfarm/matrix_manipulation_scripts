import pandas as pd
import numpy as np

def truncate_and_calculate_lost_values(df):
    # Create a new dataframe to store the truncated values and lost values
    df_truncated = df.copy()
    
    # Calculate the total lost value for each row
    total_lost_value = 0
    
    # Iterate over each column in the dataframe
    for col in df.columns:
        if(col != 'Name'):
            # Truncate all non-NaN values in the current column to two decimal places using vectorized operations.
            series_diff = (df[col] - df[col].apply(lambda x: round(x,2) if not pd.isna(x) else x)).fillna(0)

            # Add up all small differences calculated above. If it is NaN then consider its value to be zero.
            
            total_lost_value += series_diff.sum()

            # Replace these truncation-removed amounts with their corresponding original ones which were removed during rounding off operation earlier.

            df_truncated.loc[:,col]=df.apply(lambda row : round(row[col],2) if not pd.isnull(row[col]) else None , axis=1).astype(object)
            

    # Create a new column named "lost_values" to hold this info 
    df_truncated['Lost Values'] = [total_lost_value]*len(df_truncated.index)

   
    return df_truncated


# Test the function
df = pd.DataFrame({'Name': ['Seth', 'Eshanta', 'Jiametryc', 'Ash', 'Wallu'],
                   'GPA': [2.43333222, 3.812, np.nan, np.nan, 2.156545], 
                   'Age': [30.6417, 56.13423, 81.3434, np.nan, 21.5673],
                   'Salary': [np.nan, 80000.2363, 41000.454, 33000.4523, 20900.4587],
                })

assert truncate_and_calculate_lost_values(df)['GPA'].iloc[0] == 2.43
assert truncate_and_calculate_lost_values(df)['Age'].iloc[1] == 56.13
assert truncate_and_calculate_lost_values(df)['Salary'].iloc[2] == 41000.45