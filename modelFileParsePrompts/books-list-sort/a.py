import pandas as pd
import numpy as np

# Load the CSV file
df = pd.read_csv("/root/code-sandbox/randomJS/matrix_manipulation_scripts/modelFileParsePrompts/books-list-sort/20240409_212816_23692_erx5r_69b94de7-4706-4fbc-b28b-4bfb0c5ab673.1.csv")

# Extract the dates from the 'Date' column
dates = df['Date'].tolist()

# Sort the dates in ascending order
dates.sort()

# Calculate the mean, median, standard deviation, and range of the dates
mean_date = np.mean(dates)
median_date = np.median(dates)
std_dev_date = np.std(dates)
range_date = max(dates) - min(dates)

# Organize the values into a dictionary
date_info = {
    'dates': dates,
    'mean': mean_date,
    'median': median_date,
    'standard deviation': std_dev_date,
    'range': range_date
}

# Print the dictionary
print(date_info)