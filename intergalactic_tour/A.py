from math import sqrt
import random

def distance(point1, point2):
    """Calculates the Euclidean distance between two points"""
    x1, y1 = point1
    x2, y2 = point2
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def generate_routes(locations, max_distance, num_routes=3):
    """
    Generates multiple interstellar travel routes with varying start points.

    Args:
        locations: A list of tuples representing (X, Y) coordinates for interstellar bodies.
        max_distance: The maximum travel distance per day.
        num_routes: The number of routes to generate.

    Returns:
        A list of dicts, where each dict contains:
          'route': A list representing a travel route
          'total_distance': The total distance of the route
    """

    routes = []
    for _ in range(num_routes):
        # Copy the locations list and use a random starting location
        unvisited = locations[:] 
        start = random.choice(unvisited)
        unvisited.remove(start) 

        route = [start]
        current = start
        total_distance = 0

        while unvisited:
            nearest = min(unvisited, key=lambda point: distance(current, point))
            dist = distance(current, nearest)

            if dist <= max_distance:
                unvisited.remove(nearest)
                route.append(nearest)
                total_distance += dist
                current = nearest
            else:  
                break  # No reachable points within max_distance 

        # Return to Earth
        total_distance += distance(current, locations[0])
        route.append(locations[0])

        routes.append({'route': route, 'total_distance': total_distance})

    return routes

def calculate_price(total_distance):
    """
    Calculates a price based on the total distance (lower distances are cheaper)
    """
    base_price = 1000  # Adjust as needed
    return base_price + (total_distance * 0.5)  # Example: Price increases with distance

# Example usage
locations = [
    (0, 0),  # Earth
    (10, 5), 
    (20, 20),
    (5, 15),
    (-10, -10)  
]
max_distance = 15
num_routes = 3 

routes = generate_routes(locations, max_distance, num_routes)

# Sort routes based on total distance and display
for i, route_info in enumerate(sorted(routes, key=lambda x: x['total_distance'])):
    price = calculate_price(route_info['total_distance'])
    print(f"Route {i+1}: {route_info['route']}")
    print(f"Total Distance: {route_info['total_distance']:.2f}")
    print(f"Price: {price:.2f} Galactic Credits\n")