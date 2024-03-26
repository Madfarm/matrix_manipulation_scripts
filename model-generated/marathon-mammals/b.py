class Mammal:
    def __init__(self, name, average_speed, marathon_record, unique_id):
        self.name = name
        self.average_speed = average_speed
        self.marathon_record = marathon_record
        self.unique_id = unique_id
        self.marathon_times = []

    def add_marathon_time(self, time):
        self.marathon_times.append(time)

    def calculate_average_marathon_time(self):
        if len(self.marathon_times) == 0:
            return 0
        return sum(self.marathon_times) / len(self.marathon_times)

    def compare_with_other_mammal(self, other_mammal):
        if self.average_speed > other_mammal.average_speed:
            return f"{self.name} is faster than {other_mammal.name}"
        elif self.average_speed < other_mammal.average_speed:
            return f"{other_mammal.name} is faster than {self.name}"
        else:
            return f"{self.name} and {other_mammal.name} have the same average speed"

    def predict_future_marathon_time(self, future_distance):
        return self.average_speed * future_distance

# Example usage
lion = Mammal("Lion", 50, 2, 1)
lion.add_marathon_time(2.5)
lion.add_marathon_time(2.7)

zebra = Mammal("Zebra", 45, 3, 2)
zebra.add_marathon_time(3.2)
zebra.add_marathon_time(3.5)

print(lion.calculate_average_marathon_time())  # Output: 2.6
print(zebra.calculate_average_marathon_time())  # Output: 3.35

print(lion.compare_with_other_mammal(zebra))  # Output: Lion is faster than Zebra

print(lion.predict_future_marathon_time(4))  # Output: 200.0
print(zebra.predict_future_marathon_time(4))  # Output: 180.0