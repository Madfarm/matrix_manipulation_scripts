import numpy as np
from scipy.stats import linregress


def linear_regression(x, y):
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    return slope, intercept, r_value**2


x = [1, 2, 3, 4, 5]
y = [2.5, 3.5, 4.5, 5.5, 6.5]


slope, intercept, r_squared = linear_regression(x, y)


assert np.isclose(slope, 1.0, atol=1e-6)
assert np.isclose(intercept, 1.5, atol=1e-6)
assert np.isclose(r_squared, 1.0, atol=1e-6)


print("Slope: ", slope)
print("Intercept: ", intercept)
print("R-squared: ", r_squared)