import math

class LocationTracker:
    def __init__(self, location1, location2):
        self.location1 = location1
        self.location2 = location2
        self.distance = self.calculate_distance()

    def calculate_distance(self):
        x1, y1 = self.location1
        x2, y2 = self.location2
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    def recalculate_distance(self):
        self.distance = self.calculate_distance()

    def __str__(self):
        return f"Location 1: {self.location1}, Location 2: {self.location2}, Distance: {self.distance}"

# Demonstration
tracker = LocationTracker([1, 2], [4, 6])
print(tracker)

tracker.location2 = [5, 7]
tracker.recalculate_distance()
print(tracker)