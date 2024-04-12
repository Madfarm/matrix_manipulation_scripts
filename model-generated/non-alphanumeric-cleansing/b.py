import pandas as pd
import numpy as np


# Create a data table
data = {
    "Column 1": ["Special_#Tea", "\U0001f69a_Delivery_Guy","\u2603_Pancakes\u2615","\u2602_Forest_Walk","\u2117_Reading_Time"],
    "Column 2": ["Happy_&\ud83d\ude00_Day", "\u23fa_5:00PM_Meeting","\u26c6_Rainy_Sunday","\u2699_Coding_Project","\u2710_Password123"],
    "Column 3": ["\ud83d\ucd04Important_File.txt", "\u2757_New_Idea!","\u266b_Play_Music!","\u2708_Celebration!","\u2310_Set_Alarm"],
    "Column 4": ['"Click_Here!"',"\ud83c\udfc6_First_Place","\u2728_Wishing_Well","\u2650_Explore","\u2733_Picture_Frame"],
    'num_col': [i for i in range(1,6)]
}


df = pd.DataFrame(data)


def clean_data(df):


    # Select only non-numerical columns
    df = df.select_dtypes(include=['object'])


    # Remove non-alphanumeric characters and replace with spaces
    df = df.apply(lambda x: x.str.replace(r'[^A-Za-z0-9\s]', ' ', regex=True))


    return df


cleaned_df = clean_data(df)


assert df.shape == (5, 5), "DataFrame must have 5 rows and 5 columns"
assert all(df.columns == ["Column 1", "Column 2", "Column 3", "Column 4","num_col"]), "Incorrect column names"


# Check if num_col is numerical and ignore it during operations
assert df['num_col'].dtype == int,"num_col should be of integer type."


# Expected DataFrame content as a NumPy array
data = [
    ["Special  Tea", "Happy     Day", "  Important File txt", " Click Here  "],
    ["  Delivery Guy", "  5 00PM Meeting", "  New Idea ", "   First Place"],
    ["  Pancakes ", "  Rainy Sunday", "  Play Music ", "  Wishing Well"],
    ["  Forest Walk", "  Coding Project", "  Celebration ", "  Explore"],
    ["  Reading Time", "  Password123", "  Set Alarm", "  Picture Frame"],
]


# Create a DataFrame from the list
expected_df = pd.DataFrame(data, columns=["Column 1", "Column 2", "Column 3", "Column 4"])


# Assert exact content match using np.array_equal
assert np.array_equal(cleaned_df, expected_df), "DataFrame content does not match expected values"