import numpy as np


def cart2polar(coordinates):
    x = coordinates[:, 0]
    y = coordinates[:, 1]
    r = np.sqrt(x**2 + y**2)
    theta = np.arctan2(y, x)
    return np.column_stack((r, theta))


coordinates = np.array([
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8],
    [9, 10],
    [-1, -2],
    [-3, -4],
    [-5, -6],
    [-7, -8],
    [-9, -10]
])


polar_coordinates = cart2polar(coordinates)
print(polar_coordinates)