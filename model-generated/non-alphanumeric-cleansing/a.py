import pandas as pd
import numpy as np


# Create a data table
data = {
    "Column 1": ["Special_#Tea", "\U0001f69a_Delivery_Guy","\u2603_Pancakes\u2615","\u2602_Forest_Walk","\u2117_Reading_Time"],
    "num_col" : [1,2,3,4,5],
    "Column 2": ["Happy_&\ud83d\ude00_Day", "\u23fa_5:00PM_Meeting","\u26c6_Rainy_Sunday","\u2699_Coding_Project","\u2710_Password123"],
    "Column 3": ["\ud83d\ucd04Important_File.txt", "\u2757_New_Idea!","\u266b_Play_Music!","\u2708_Celebration!","\u2310_Set_Alarm"],
    "Column 4": ['"Click_Here!"',"\ud83c\udfc6_First_Place","\u2728_Wishing_Well","\u2650_Explore","\u2733_Picture_Frame"]
}


df = pd.DataFrame(data)


def clean_data(df):


    # Find numeric columns and exclude them from the cleaning process
    non_numeric_cols = df.select_dtypes(exclude=[np.number]).columns


    # Remove non-alphanumeric characters and replace with spaces for string cols
    df[non_numeric_cols] = df[non_numeric_cols].apply(lambda x: x.str.replace(r'[^A-Za-z0-9\s]', ' ', regex=True))
    return df


cleaned_df = clean_data(df)


assert df.shape == (5, 5), "DataFrame must have 5 rows and 5 columns"
assert all(df.columns == ["Column 1", "num_col","Column 2", "Column 3", "Column 4"]), "Incorrect column names"
# Check if all data types are correct 
assert df.dtypes.equals(pd.Series({"Column 1":object,"num_col":int ,"Column 2": object , "Column 3": object , "Column 4": object})), f"All dtypes do not match {df.dtypes}"


# Expected DataFrame content as a NumPy array
data = [
    ["Special  Tea",1, "Happy     Day", "  Important File txt", " Click Here  "],
    ["  Delivery Guy",2, "  5 00PM Meeting", "  New Idea ", "   First Place"],
    ["  Pancakes ",3, "  Rainy Sunday", "  Play Music ", "  Wishing Well"],
    ["  Forest Walk",4, "  Coding Project", "  Celebration ", "  Explore"],
    ["  Reading Time",5, "  Password123", "  Set Alarm", "  Picture Frame"],
]



# Create a DataFrame from the list
expected_df = pd.DataFrame(data, columns=["Column 1",'num_col',"Column 2", "Column 3", "Column 4"])


# Assert exact content match using np.array_equal
assert np.array_equal(cleaned_df.values, expected_df.values), "DataFrames content does not match exactly"