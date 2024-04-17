import pandas as pd


# Define the input DataFrame
df = pd.DataFrame(["STD, City    State",
"33, Kolkata    West Bengal",
"44, Chennai    Tamil Nadu",
"40, Hyderabad    Telengana",
"80, Bangalore    Karnataka"], columns=['row'])


# Split the strings into new columns
df[['STD', 'City', 'State']] = df['row'].str.extract(r'(\d+),\s*(\w+)\s+(\w+)', expand=True)


# Drop the original column
df = df.drop('row', axis=1)


# Print the resulting DataFrame
print(df)
print(df['State'].iloc[1])


assert df['STD'].dtype == 'object'
assert df['City'].dtype == 'object'
assert df['State'].dtype == 'object'

assert df['STD'].iloc[1] == '33'
assert df['City'].iloc[1] == 'Kolkata'
assert df['State'].iloc[1] == 'West Bengal'


assert df['STD'].iloc[1] == 44
assert df['City'].iloc[1] == 'Chennai'
assert df['State'].iloc[1] == 'Tamil Nadu'


assert df['STD'].iloc[2] == 40
assert df['City'].iloc[2] == 'Hyderabad'
assert df['State'].iloc[2] == 'Telengana'


assert df['STD'].iloc[3] == 80
assert df['City'].iloc[3] == 'Bangalore'
assert df['State'].iloc[3] == 'Karnataka'