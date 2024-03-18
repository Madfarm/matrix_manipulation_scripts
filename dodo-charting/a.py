import math

class DodoBird:
    def __init__(self):
        self.continents = {
            "Africa": (0, 0),
            "Antarctica": (0, -10),
            "Asia": (10, 0),
            "Australia": (10, -10),
            "Europe": (0, 5),
            "North America": (-10, 5),
            "South America": (-10, 0)
        }
        self.speed = 100  # km/h
        self.rest_time = 8  # hours
        self.travel_time = 16  # hours

    def distance(self, x1, y1, x2, y2):
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def time_required(self, distance):
        return distance / self.speed

    def get_optimal_route(self):
        optimal_route = []
        visited_continents = []
        current_location = "Africa"  # Start from Africa
        total_time = 0

        while len(visited_continents) < 7:
            closest_continent = None
            shortest_distance = float('inf')

            for continent, coordinates in self.continents.items():
                if continent not in visited_continents:
                    distance = self.distance(self.continents[current_location][0], self.continents[current_location][1], coordinates[0], coordinates[1])
                    if distance < shortest_distance:
                        shortest_distance = distance
                        closest_continent = continent

            time_to_next_continent = self.time_required(shortest_distance)
            if total_time + time_to_next_continent > self.travel_time:
                total_time += self.rest_time
            total_time += time_to_next_continent

            visited_continents.append(closest_continent)
            optimal_route.append(closest_continent)
            current_location = closest_continent

        return optimal_route, total_time


dodo = DodoBird()
optimal_route, total_time = dodo.get_optimal_route()
print("Optimal route: ", optimal_route)
print("Total time: ", total_time, "hours")