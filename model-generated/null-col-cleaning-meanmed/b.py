import pandas as pd
import numpy as np


# Create a sample DataFrame with null values and NaNs
df = pd.DataFrame({'Name': ['Seth', 'Eshanta', 'Jiametryc', 'Ash', 'Wallu'],
                   'GPA': [2.4, 3.8, np.nan, np.nan, 2.1], 
                   'Age': [30, 56, 81, np.nan, 21],
                   'Salary': [np.nan, 80000, 41000, 33000, 20900],
                   'Birthday': [None,None,None,None, None]})


# Replace all nan values with 0s
df.fillna(0, inplace=True)


# Remove columns that contain only zeros or nulls (in this case Birthday)
df.replace({None: np.nan}, inplace=True) #Replace remaining none values to nan for dropna() method.
df.dropna(axis=1, how='all', inplace=True)


def get_mean_and_median(df):
    mean_dict = df.mean().to_dict()
    median_dict = df.median().to_dict()


    return {col: {"mean": round(mean_val, 3), "median": round(median_val, 3)} for col, mean_val in mean_dict.items() for _, median_val in median_dict.items() if _ == col}


output_dict = get_mean_and_median(df)


assert output_dict['GPA']["mean"] == round((2.4 + 3.8 + 0 + 0 + 2.1)/5 ,3), f"Expected GPA's mean value is {(2.4 + 3.8 + 0 + 0 + 2.1)/5} but got {output_dict['GPA']['mean']}"


assert output_dict['Age']["mean"] == round((30+56+81+0+21)/5,3), f"Expected Age's mean value is {(30+56+81+0+21)/5} but got {output_dict['Age']['mean']}"
assert output_dict['Age']["median"]==round(30,3), f"Expected Age's median value is 30 but got {output_dict['Age']['median']}"


print(output_dict)