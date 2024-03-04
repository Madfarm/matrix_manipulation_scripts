import random
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

def generate_random_route(locations, max_distance):
    """
    Generates a random interstellar travel route.

    This function shuffles the order of locations before applying the Nearest Neighbor heuristic
    to create a varied route.
    """
    randomized_locations = locations.copy()  # Create a copy to preserve original list
    random.shuffle(randomized_locations)
    return nearest_neighbor(randomized_locations, max_distance)

def calculate_total_distance(route):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distance(route[i], route[i+1])
    return total_distance

def price_route(total_distance):
    # Implement pricing logic here. For demonstration purposes, 
    # let's consider a base price of 100 space credits per distance unit, 
    # with a discount for longer routes
    base_price = 100
    discount_factor = 0.001  # Adjust as needed
    return base_price * total_distance * (1 - discount_factor * total_distance)

def display_routes(routes):
    for i, route in enumerate(routes):
        total_distance = calculate_total_distance(route)
        price = price_route(total_distance)
        print(f"Route {i+1}: {route}, Total Distance: {total_distance:.2f}, Price: {price:.2f} space credits")

# Generate multiple routes
locations = [
    (0, 0),  # Earth (starting point)
    (10, 5),  # Planet X
    (20, 20),  # Star Y
    (5, 15),  # Asteroid Z
    (-10, -10)  # Black Hole W
]
max_distance = 15        
        
num_routes = 3
max_distance = 15
all_routes = [generate_random_route(locations, max_distance) for _ in range(num_routes)]

# Display routes with distances and prices
display_routes(all_routes)
