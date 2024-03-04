from math import sqrt
import random
import os

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

def display_menu(routes, balance):
    """Displays a console menu for the user to interact with"""
    os.system('clear')  # Clear the console
    print(f"Galactic Travel Agency - Balance: {balance:.2f} Galactic Credits")
    print("Available Routes:")
    for i, route_info in enumerate(routes):
        price = calculate_price(route_info['total_distance'])
        print(f"[{i+1}] Distance: {route_info['total_distance']:.2f} - Price: {price:.2f}")

    print("[Q] Quit")

def main():
    """Main function to handle user interaction and route purchasing"""
    locations = [
        (0, 0),  # Earth (starting point)
        (10, 5),  # Planet X
        (20, 20),  # Star Y
        (5, 15),  # Asteroid Z
        (-10, -10)  # Black Hole W
    ]
    max_distance = 15
    num_routes = 3
    user_balance = 10000.0  # Starting balance

    while True:
        routes = generate_routes(locations, max_distance, num_routes)
        display_menu(routes, user_balance)

        choice = input("Select a route to purchase or press 'Q' to quit: ")

        if choice.upper() == 'Q':
            break

        if not choice.isdigit() or int(choice) not in range(1, num_routes+1):
            print("Invalid choice. Please select a valid route number or 'Q' to quit.")
            continue
        
        selected_route = routes[int(choice)-1]
        price = calculate_price(selected_route['total_distance'])

        if price <= user_balance:
            user_balance -= price
            print(f"You purchased Route {choice} for {price:.2f} Galactic Credits! Enjoy your trip!")
            print(f"Your new balance is: {user_balance:.2f} Galactic Credits")
        else:
            print("Insufficient funds! Please select a different route or top up your balance.")

if __name__ == "__main__":
    main()