import numpy as np

def linear_regression(x, y):
    # Calculate the mean of x and y
    mean_x = np.mean(x)
    mean_y = np.mean(y)

    # Calculate the deviations from the mean
    dev_x = x - mean_x
    dev_y = y - mean_y

    # Calculate the slope (beta1) and intercept (beta0)
    beta1 = np.sum(dev_x * dev_y) / np.sum(dev_x ** 2)
    beta0 = mean_y - beta1 * mean_x

    return beta0, beta1

# Example usage:
x = np.array([2019, 2020, 2021, 2022])  # Years
y = np.array([39507, 39507, 39507, 39507])  # Fatal car crashes involving alcohol

# Perform linear regression
beta0, beta1 = linear_regression(x, y)

# Print the results
print("Intercept (beta0):", beta0)
print("Slope (beta1):", beta1)