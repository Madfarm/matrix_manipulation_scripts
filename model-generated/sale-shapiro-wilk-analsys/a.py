import numpy as np
from scipy.stats import shapiro


# Define the sales data
sales_data = [10000, 12700, 11500, 13300, 13900, 15100, 16999, 17200, 18100, 18500, 20500, 21500]


# Calculate the total sales for the year
total_sales = sum(sales_data)
assert total_sales == 201199


# Calculate the monthly average sales
average_sales = total_sales / len(sales_data)
assert average_sales == 16766.583333333332


# Identify the month with the highest sales
highest_sales_month = np.argmax(sales_data) + 1  # Add 1 to convert from 0-indexed to 1-indexed month
assert highest_sales_month == 12


# Find the month-to-month percentage change in sales
percentage_change = [(sales_data[i] - sales_data[i-1]) / sales_data[i-1] * 100 for i in range(1, len(sales_data))]
assert percentage_change == [27.0, -9.44954128440367, 15.652173913043478, 4.5112781954887215, 8.633093525179856, 13.298025477707006, 1.0638297872340422, 5.233918128654971, 2.2026431718061676, 10.81081081081081, 4.878048780487805]


# Test whether the sales data follow a normal distribution using a Shapiro-Wilk test
w_stat, p_value = shapiro(sales_data)
assert w_stat == 0.9668962955474854
assert p_value == 0.8757304549217224