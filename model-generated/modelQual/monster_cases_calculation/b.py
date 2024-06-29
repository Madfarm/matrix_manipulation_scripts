import random

# Define the initial amount spent on utilities in 2024
initial_amount = 520.88

# Define the price of a case of Ultra Fantasy Ruby Red
case_price = 26.56

# Calculate the number of cases that can be bought with the initial amount
initial_cases = initial_amount / case_price

# Initialize the total number of cases
total_cases = initial_cases

# Loop through the years from 2025 to 2026
for year in range(2025, 2027):
    # Randomly increase the amount spent on utilities by 1-100
    increase = random.randint(1, 100)
    new_amount = initial_amount + increase
    
    # Calculate the number of cases that can be bought with the new amount
    new_cases = new_amount / case_price
    
    # Add the new cases to the total number of cases
    total_cases += new_cases

# Print the total number of cases
print(total_cases)