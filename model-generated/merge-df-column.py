import pandas as pd


# Create the first data frame
Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]}
df1 = pd.DataFrame(Car_Price)


# Create the second data frame
car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 , 160]}
df2 = pd.DataFrame(car_Horsepower)


# Merge the two data frames
df = pd.merge(df1, df2, on='Company')


# Print the merged data frame
print(df)