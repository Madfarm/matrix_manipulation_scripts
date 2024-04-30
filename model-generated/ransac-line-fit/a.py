import numpy as np
from numba import njit

@njit
def calculate_distances(x, y, slope, intercept):
    return np.abs(y - (slope * x + intercept)) / np.sqrt(slope**2 + 1)

best_inliers = 0
best_slope = 0
best_intercept = 0

for _ in range(max_iter):
    # Randomly select two points
    indices = np.random.randint(0, len(x), 2)
    
    # Calculate the slope and intercept of the line through these two points
    x1, x2 = x[indices]
    y1, y2 = y[indices]
    slope = (y2 - y1) / (x2 - x1)
    intercept = y1 - slope * x1
    
    # Calculate the distance of all points from this line
    distances = calculate_distances(x, y, slope, intercept)
    
    # Count the number of inliers (points with distance less than the threshold)
    inliers = np.sum(distances < threshold)
    
    # If this line has more inliers than any previous line, save it
    if inliers > best_inliers:
        best_inliers = inliers
        best_slope = slope
        best_intercept = intercept


# Test the function
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([2.5, 3.5, 4.7, 5.3, 6.2, 6.8, 8.2, 9.5, 10.1, 11.5])


slope, intercept = ransac_line_fit(x, y)


assert isinstance(slope, float), "Slope should be a float"
assert isinstance(intercept, float), "Intercept should be a float"