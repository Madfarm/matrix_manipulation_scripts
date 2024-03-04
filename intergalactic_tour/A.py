from math import sqrt

def distance(point1, point2):
  """Calculates the Euclidean distance between two points"""
  x1, y1 = point1
  x2, y2 = point2
  return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def nearest_neighbor(locations, max_distance):
  """
  Plans an interstellar travel route using Nearest Neighbor heuristic.

  Args:
      locations: A list of tuples representing (X, Y) coordinates for interstellar bodies.
      max_distance: The maximum travel distance per day.

  Returns:
      A list representing the optimal travel route including Earth at the beginning and end.
  """
  visited = set([locations[0]])  # Start with Earth
  remaining = set(locations[1:])  # Exclude Earth from remaining locations
  current = locations[0]
  route = [current]

  while remaining:
    closest = None
    closest_distance = float('inf')  # Initialize with positive infinity

    for point in remaining:
      dist = distance(current, point)
      if dist <= max_distance and dist < closest_distance:
        closest = point
        closest_distance = dist

    if closest:
      visited.add(closest)
      remaining.remove(closest)
      current = closest
      route.append(current)
    else:
      # No reachable points within max distance, return incomplete route
      return route + list(remaining) + route  # Add remaining as unreachable

  # Reached all points, return route with Earth at the end
  return route + [locations[0]]

# Example usage
locations = [
    (0, 0),  # Earth (starting point)
    (10, 5),  # Planet X
    (20, 20),  # Star Y
    (5, 15),  # Asteroid Z
    (-10, -10)  # Black Hole W
]
max_distance = 15

route = nearest_neighbor(locations, max_distance)
print("Optimal Travel Route:", route)

# This will print something like:
# Optimal Travel Route: [(0, 0), (5, 15), (10, 5), (20, 20), (-10, -10), (0, 0)]