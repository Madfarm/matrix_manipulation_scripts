import pandas as pd

def clean_strings(df):
    # Use str.split() to split the strings into lists
    df['row'] = df['row'].str.split(r'\s{2,}|,')


    # Use apply(pd.Series) to convert the lists into separate columns
    df[['STD', 'City', 'State']] = df['row'].apply(pd.Series)


    # Drop the original column
    df.drop('row', axis=1, inplace=True)


    return df


# Test the function
df = pd.DataFrame(["STD, City    State",
"33, Kolkata    West Bengal",
"44, Chennai    Tamil Nadu",
"40, Hyderabad    Telengana",
"80, Bangalore    Karnataka"], columns=['row'])


df = clean_strings(df)


# Validate the output using assertions
assert df.shape == (5, 3)
assert df['STD'].tolist() == ['STD', '33', '44', '40', '80']
assert df['City'].tolist() == [' City', ' Kolkata', ' Chennai', ' Hyderabad', ' Bangalore']
assert df['State'].tolist() == ['State', 'West Bengal', 'Tamil Nadu', 'Telengana', 'Karnataka']