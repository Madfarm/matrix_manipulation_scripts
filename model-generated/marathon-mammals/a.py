import math

class Mammal:
    def __init__(self, name, speed, record, unique_id):
        self.name = name
        self.speed = speed  # in miles per hour
        self.record = record  # in minutes
        self.unique_id = unique_id
        self.marathon_times = []

    def add_marathon_time(self, time):
        self.marathon_times.append(time)

    def calculate_average_marathon_time(self):
        if not self.marathon_times:
            return 0
        return sum(self.marathon_times) / len(self.marathon_times)

    def compare_with_other_mammal(self, other_mammal):
        if self.record < other_mammal.record:
            return f"{self.name}'s record is faster than {other_mammal.name}'s record."
        elif self.record > other_mammal.record:
            return f"{self.name}'s record is slower than {other_mammal.name}'s record."
        else:
            return f"{self.name}'s record is equal to {other_mammal.name}'s record."

    def predict_future_marathon_time(self, distance):
        # Assuming the marathon time is inversely proportional to the speed
        # and the distance remains constant for all mammals
        time = (distance / self.speed) * 60  # convert hours to minutes
        return time


# Example usage
cheetah = Mammal("Cheetah", 70, 20, 1)
cheetah.add_marathon_time(20)
cheetah.add_marathon_time(22)
print(f"{cheetah.name}'s average marathon time is: {cheetah.calculate_average_marathon_time()} minutes")

lion = Mammal("Lion", 30, 35, 2)
print(cheetah.compare_with_other_mammal(lion))

distance = 26.2  # marathon distance in miles
print(f"{cheetah.name}'s predicted marathon time for a {distance} miles distance is: {cheetah.predict_future_marathon_time(distance)} minutes")