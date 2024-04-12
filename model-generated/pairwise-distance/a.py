import numpy as np
from scipy.spatial import distance


# Define the points in set A and B
points_A = np.array([
    [4.89975235, 2.47860124],
    [3.38739576, 2.56809379],
    [5.16727473, 7.66779772],
    [2.92089192, 0.9130243 ],
    [7.56719067, 9.95741173]
])


points_B = np.array([
    [8.76755107, 3.1092104 ],
    [9.52452436, 7.17733301],
    [8.21593371, 9.20997495],
    [0.23208664, 4.41050725],
    [7.85738209, 4.76088395],
    [9.63034932, 1.44517336],
    [9.56476609, 0.43346803],
    [9.2772763 , 2.82445653],
    [7.1781618 , 0.19147048]
])


def find_closest_point(points_A, point):
    # Calculate pairwise distances between all points in set A and a specific point from set B
    dists = distance.cdist([point], points_A)[0]


    # Find index of minimum distance (i.e., closest point)
    idx_min_dist = np.argmin(dists)


    return points_A[idx_min_dist]


closest_points = []
for i, b in enumerate(points_B): 
    
    result = find_closest_point(points_A, b)
  
    assert isinstance(result, np.ndarray), f'Expected output type list but got {type(result)}'
    assert len(result) == 2, 'Invalid number of dimensions for result'

    closest_points.append(result)

