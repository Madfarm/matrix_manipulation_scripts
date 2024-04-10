import pandas as pd
import numpy as np


# Define the original DataFrame
df = pd.DataFrame({'Name': ['Seth', 'Eshanta', 'Jiametryc', 'Ash', 'Wallu'],
                   'GPA': [2.4, 3.8, np.nan, np.nan, 2.1], 
                   'Age': [30, 56, 81, np.nan, 21],
                   'Salary': [np.nan, 80000, 41000, 33000, 20900],
                })


# Function to generate random data
def generate_random_data(df):
    # Calculate the number of rows to add
    rows_to_add = 50 - len(df)


    # Define the data types for each column
    data_types = {
        'Name': str,
        'GPA': float,
        'Age': float,
        'Salary': float
    }


    # Generate random data for each column
    random_data = {
        col: [np.random.choice(df[col].dropna()) if data_types[col] == str else np.random.uniform(df[col].dropna().min(), df[col].dropna().max()) for _ in range(rows_to_add)]
        for col in df.columns
    }


    # Create a new DataFrame with the random data
    new_df = pd.DataFrame(random_data)


    # Append the new DataFrame to the original DataFrame
    df = pd.concat([df, new_df], ignore_index=True)


    return df


# Call the function to add rows to the DataFrame
df = generate_random_data(df)


# Print the updated DataFrame
print(df)