class Planet:
    def __init__(self, name, day_length, year_length, num_moons, avg_temp, gravity, distance_from_sun):
        self.name = name
        self.day_length = day_length
        self.year_length = year_length
        self.num_moons = num_moons
        self.avg_temp = avg_temp
        self.gravity = gravity
        self.distance_from_sun = distance_from_sun

    def calculate_time_difference(self, other_planet):
        # Calculate the time difference between two planets
        time_diff = self.day_length / other_planet.day_length
        return time_diff

    def calculate_fuel_needed(self, other_planet):
        # Calculate the fuel needed based on the distance and gravity
        distance = self.distance_from_sun - other_planet.distance_from_sun
        print(distance)
        fuel_needed = distance * self.gravity * other_planet.gravity
        return fuel_needed


# Create instances of the Planet class
earth = Planet('Earth', 24, 365, 1, 15, 9.8, 149.6)
mars = Planet('Mars', 24.6, 687, 2, -67, 3.7, 227.9)

# Calculate time difference and fuel needed
time_diff = earth.calculate_time_difference(mars)
fuel_needed = earth.calculate_fuel_needed(mars)

print(f"Time difference between Earth and Mars: {time_diff} times")
print(f"Fuel needed to travel from Earth to Mars: {fuel_needed} units")