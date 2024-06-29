import random

# Set the initial utility bill and the price of a case of Monster Ultra Fantasy Ruby Red
utility_bill = 520.88
case_price = 26.56

# Set the number of years to calculate
years = 2

# Initialize the total number of cases
total_cases = 0

# Loop through each year
for year in range(years):
    # Randomly increase the utility bill by 1-100
    utility_bill += random.randint(1, 100)
    
    # Calculate the number of cases that can be bought with the utility bill
    cases = utility_bill // case_price
    
    # Add the number of cases to the total
    total_cases += cases

# Print the total number of cases
print(total_cases)