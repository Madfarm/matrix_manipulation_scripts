import pandas as pd


# Define the dictionaries
GermanCars = {'Company': ['Ford', 'Mercedes', 'BMW', 'Audi'], 'Price': [23845, 171995, 135925, 71400]}
JapaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi'], 'Price': [29995, 23600, 61500, 58900]}


# Create data frames from the dictionaries
df_GermanCars = pd.DataFrame(GermanCars)
df_JapaneseCars = pd.DataFrame(JapaneseCars)


# Concatenate the two data frames
df_Cars = pd.concat([df_GermanCars, df_JapaneseCars], keys=['German Cars', 'Japanese Cars'])


# Print the concatenated data frame
print(df_Cars)