import pandas as pd
import numpy as np


# Creating the dataframe
df = pd.DataFrame({'Name': ['Seth', 'Eshanta', 'Jiametryc', 'Ash', 'Wallu'],
                   'GPA': [2.4, 3.8, np.nan, np.nan, 2.1], 
                   'Age': [30, 56, 81, np.nan, 21],
                   'Salary': [np.nan, 80000, 41000, 33000, 20900],
                   'Birthday': [None,None,None,None, None]})


# Function to clean and process the data
def clean_data(df):

    # Remove columns that have all null or missing values
    for col in list(df.columns[df.isnull().all()]):
        del df[col]

    # Replace NaN values with 0
    df.fillna(0, inplace=True)

    # Calculate mean and median of each column after replacing nan with zero
    stats_dict = {}
    for col in df.columns:
        if col != 'Name':
            stats_dict[col+'_mean'] = df[col].mean()
            stats_dict[col+'_median'] = df[col].median()

    return df,stats_dict


# Call function on our original DataFrame.
new_df,new_stats=clean_data(df.copy())


# We use copy() above because we need to verify new_df against df below.


assert(new_df.equals(pd.DataFrame({
                    "Name":['Seth','Eshanta','Jiametryc','Ash','Wallu'], 
                    "GPA" :[2.4 ,3.8,   0.0,     0.0,      2.1 ],
                    "Age" :[30.0, 56.0, 81.0,   0.0,  21.0],
                    "Salary":[  0.0,  80000, 41000, 33000, 20900]})))


assert(new_stats == {'GPA_mean': 1.6599999999999997,
                     'GPA_median': 2.1,
                     'Age_mean': 37.6,
                     'Age_median': 30.0,
                     'Salary_mean': 34980.0,
                     'Salary_median': 33000.0})