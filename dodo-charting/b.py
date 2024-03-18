import math

class Dodo:
    def __init__(self):
        self.speed = 100  # km/h, average flight speed
        self.max_distance = 16 * self.speed  # km, max distance Dodo can fly in one stretch
        self.rest_time = 8  # h, time Dodo needs to rest after flying
        self.locations = {
            'Africa': (0, 0),
            'Antarctica': (0, 10),
            'Asia': (10, 0),
            'Australia': (10, 10),
            'Europe': (5, 5),
            'North America': (3, 3),
            'South America': (7, 7)
        }

    def distance(self, loc1, loc2):
        x1, y1 = self.locations[loc1]
        x2, y2 = self.locations[loc2]
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    def plan_trip(self):
        visited = ['Africa']
        to_visit = list(self.locations.keys())
        to_visit.remove('Africa')
        total_distance = 0
        total_time = 0

        while to_visit:
            closest = min(to_visit, key=lambda loc: self.distance(visited[-1], loc))
            to_visit.remove(closest)
            distance_to_next = self.distance(visited[-1], closest)
            total_distance += distance_to_next
            time_to_next = distance_to_next / self.speed
            total_time += time_to_next
            if total_time % (self.max_distance / self.speed + self.rest_time) >= self.max_distance / self.speed:
                total_time += self.rest_time
            visited.append(closest)

        return visited, total_distance, total_time

dodo = Dodo()
visited, total_distance, total_time = dodo.plan_trip()
print(f"Dodo's trip: {' -> '.join(visited)}")
print(f"Total distance: {total_distance} km")
print(f"Total time: {total_time} h")