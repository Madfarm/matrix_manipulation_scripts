
import numpy as np


def cartesian_to_polar(coordinates):
    # Calculate the radius
    r = np.sqrt(coordinates[:, 0]**2 + coordinates[:, 1]**2)


    # Calculate the angle
    theta = np.arctan2(coordinates[:, 1], coordinates[:, 0])


    # Combine the radius and angle into a 10x2 array
    polar_coordinates = np.stack((r, theta), axis=1)


    return polar_coordinates


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


polar_coordinates = cartesian_to_polar(coordinates)
print(polar_coordinates)