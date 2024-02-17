import random
import math

class Bird:
    def __init__(self, species, start_location, destination, speed, preferred_weather):
        self.species = species
        self.start_location = start_location  # tuple (lat, lon)
        self.destination = destination  # tuple (lat, lon)
        self.speed = speed  # meters per second
        self.preferred_weather = preferred_weather  # list of weather conditions (e.g. ["sunny", "windy"])
        self.current_location = start_location
        self.pitstops = []  # list of tuples (lat, lon, distance_traveled)

    def __str__(self):
        return f"{self.species} migrating from {self.start_location} to {self.destination} at {self.speed} m/s"

def simulate_migration(bird, num_days, weather_data):
    """
    Simulate the bird's migration journey over num_days days.
    weather_data is a list of daily weather conditions (each a string)
    """
    for day in range(num_days):
        # Get the current weather condition
        weather = weather_data[day]

        # Check if the bird wants to migrate today based on the weather
        if weather in bird.preferred_weather:
            # Calculate the distance to travel today
            distance = bird.speed * 86400  # convert speed from m/s to km/day

            # Get the direction to travel (towards destination)
            direction = math.radians(bird.destination[0] - bird.current_location[0])

            # Simulate traveling and check for pitstops
            while distance > 0:
                # Check if there is a geographic feature (e.g. mountain, river) within the bird's range
                # If so, make a pitstop and adjust the distance accordingly
                # (Note: this is a simplified implementation, you could use more sophisticated algorithms to determine pitstops)
                if random.random() < 0.1:  # 10% chance of encountering a geographic feature
                    distance -= 100  # make a pitstop and reduce distance traveled
                    bird.pitstops.append((bird.current_location[0], bird.current_location[1], distance))

                # Update the bird's location
                bird.current_location = (bird.current_location[0] + distance * math.cos(direction),
                                         bird.current_location[1] + distance * math.sin(direction))
                distance -= distance  # reduce distance traveled to 0

            # Update the bird's pitstops
            bird.pitstops.append((bird.current_location[0], bird.current_location[1], 0))

    return bird

# Example usage:
weather_data = ["sunny", "cloudy", "rain", "windy", "sunny", "cloudy"]
bird = Bird("Robin", (40.0, -100.0), (30.0, -80.0), 10, ["sunny", "windy"])
simulated_bird = simulate_migration(bird, 6, weather_data)
print(simulated_bird)
print(simulated_bird.pitstops)