import pandas as pd


# Create the DataFrame
df = pd.DataFrame(["STD, City    State",
"33, Kolkata    West Bengal",
"44, Chennai    Tamil Nadu",
"40, Hyderabad    Telengana",
"80, Bangalore    Karnataka"], columns=['row'])


# Split the string column into three columns
df = df['row'].str.split(',|    ', expand=True)


# Rename the columns
df.columns = ['STD', 'City', 'State']


print(df)