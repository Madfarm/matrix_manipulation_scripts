import scipy.spatial.distance as distance
import numpy as np


def closest_point(points_a, points_b, target_point):
    # Calculate pairwise distances between points in set A and B
    dists = distance.cdist(points_a, points_b)


    # Find the index of the point with minimum distance to the target point
    min_index = np.argmin(dists[target_point])


    return min_index


# Define two sets of 2D points
points_set1 = [(4.89975235, 2.47860124), (3.38739576, 2.56809379),
               (5.16727473, 7.66779772), (2.92089192, 0.9130243)]
points_set2 = [(9.52452436, 7.17733301),(8.21593371, 9.20997495)]


# Convert them into numpy arrays for efficient computation
points_array1 = np.array(points_set1)
points_array2 = np.array(points_set2)


target = (9.2772763, 2.82445653)  # Target point
closest_idx = closest_point(points_array1, points_array2, target)


print(f"Closest point from first set is: {points_array1[closest_idx]}")
print("Correct output:")
print("The Closest point from first set is:",(4.89975235,2.47860124))