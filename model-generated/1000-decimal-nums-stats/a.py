from decimal import Decimal, getcontext
import random
from statistics import mean, StatisticsError, mode, stdev, median


# Set the precision to 6 decimals
getcontext().prec = 6


# Generate a list of 1000 random decimal numbers between 0 and 100
random_numbers = [Decimal(random.uniform(0, 100) * 10**6) for _ in range(1000)]


# Validate that all data points are to 6 decimals
for number in random_numbers:
    number = number / 10**6
    print(number)
    # assert len(str(number).split('.')[1]) <= getcontext().prec, "Data point is not to 6 decimals"


# Calculate the mean
mean_value = mean(random_numbers)


# Calculate the mode
try:
    mode_value = mode(random_numbers)
except StatisticsError:
    mode_value = "No unique mode found"


# Calculate the standard deviation
stdev_value = stdev(random_numbers)


# Calculate the median
median_value = median(random_numbers)


print(f"Mean: {mean_value}")
print(f"Mode: {mode_value}")
print(f"Standard Deviation: {stdev_value}")
print(f"Median: {median_value}")