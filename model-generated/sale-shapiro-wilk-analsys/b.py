import numpy as np
from scipy.stats import shapiro


# Dataset
sales_data = [10000, 12000, 11000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000]


# Calculate total sales for the year
total_sales = sum(sales_data)
assert total_sales == 186000


# Determine the monthly average sales
monthly_average_sales = total_sales / len(sales_data)
assert monthly_average_sales == 15500.0


# Identify the month with the highest sales
highest_sales_month = sales_data.index(max(sales_data)) + 1
assert highest_sales_month == 12


# Find the month-to-month percentage change in sales
percentage_change = [(sales_data[i] - sales_data[i-1]) / sales_data[i-1] * 100 for i in range(1, len(sales_data))]
assert percentage_change == [20.0, -8.333333333333332, 18.181818181818183, 7.6923076923076925, 7.142857142857142, 6.666666666666667, 6.25, 5.88235294117647, 5.555555555555555, 5.263157894736842, 5.0]


# Test whether the sales data follow a normal distribution using a Shapiro-Wilk test
normality_test_result = shapiro(sales_data)
assert normality_test_result.statistic == 0.9668962955474854
assert normality_test_result.pvalue == 0.8757304549217224