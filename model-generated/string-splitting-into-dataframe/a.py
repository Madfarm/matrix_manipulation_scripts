import pandas as pd


# Create a DataFrame
df = pd.DataFrame(["STD, City    State",
"33, Kolkata    West Bengal",
"44, Chennai    Tamil Nadu",
"40, Hyderabad    Telengana",
"80, Bangalore    Karnataka"], columns=['row'])


# Split the string column into 3 columns
df[['STD', 'City', 'State']] = df['row'].str.split(',', expand=True)


# Drop the original 'row' column
df.drop(columns=['row'], inplace=True)


# Strip leading and trailing spaces from 'City' and 'State' columns
df['City'] = df['City'].str.strip()
df['State'] = df['State'].str.strip()


# Print the resulting DataFrame
print(df)


