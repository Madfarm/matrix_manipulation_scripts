import random
import math

class Bird:
    def __init__(self, species, start_location, destination, speed, preferred_weather):
        self.species = species
        self.start_location = start_location
        self.destination = destination
        self.speed = speed
        self.preferred_weather = preferred_weather
        self.current_location = start_location
        self.pitstops = []

    def __repr__(self):
        return f"{self.species} migrating from {self.start_location} to {self.destination}"

def simulate_migration(bird, num_days, weather_data):
    for day in range(num_days):
        # Calculate distance to travel based on speed and weather conditions
        distance = bird.speed * (weather_data[day]["wind_speed"] + 1)
        direction = math.radians(weather_data[day]["wind_direction"])
        x, y = bird.current_location
        dx, dy = math.cos(direction), math.sin(direction)
        new_x, new_y = x + distance * dx, y + distance * dy
        bird.current_location = (new_x, new_y)

        # Check for pitstops based on geographic features and weather conditions
        if weather_data[day]["precipitation"] > 0.5:
            # Avoid flying in heavy rain, take a pitstop
            bird.pitstops.append((new_x, new_y))
            bird.current_location = bird.pitstops[-1]
        elif geographic_features(new_x, new_y) == "mountain":
            # Avoid flying over mountains, take a pitstop
            bird.pitstops.append((new_x, new_y))
            bird.current_location = bird.pitstops[-1]

        # Update bird's magnetic field and sun position
        bird.update_magnetic_field(new_x, new_y)
        bird.update_sun_position(day)

        # Check if reached destination
        if bird.current_location == bird.destination:
            print(f"{bird} reached destination after {day+1} days")
            return

def geographic_features(x, y):
    # Simulate a simple geographic feature map
    features = {
        (0, 0): "ocean",
        (0, 100): "mountain",
        (100, 0): "desert",
        (100, 100): "forest"
    }
    return features.get((x, y), "unknown")

def generate_weather_data(num_days):
    # Simulate a simple weather data generator
    weather = []
    for day in range(num_days):
        weather.append({
            "wind_speed": random.uniform(0, 10),
            "wind_direction": random.uniform(0, 360),
            "precipitation": random.uniform(0, 1)
        })
    return weather

# Example usage
bird = Bird("Robin", (0, 0), (100, 100), 50, ["sunny", "light_wind"])
weather_data = generate_weather_data(30)
simulate_migration(bird, 30, weather_data)