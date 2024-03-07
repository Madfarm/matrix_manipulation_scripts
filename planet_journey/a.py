class Planet:
    def __init__(self, name, day_length, year_length, num_moons, avg_temp, gravity, distance_from_sun):
        self.name = name
        self.day_length = day_length
        self.year_length = year_length
        self.num_moons = num_moons
        self.avg_temp = avg_temp
        self.gravity = gravity
        self.distance_from_sun = distance_from_sun

    def calc_time_difference(self, other_planet):
        # Calculate the time difference between two planets
        time_diff = self.day_length / other_planet.day_length
        return time_diff

    def calc_fuel_needed(self, other_planet):
        # Calculate the fuel needed based on the distance and gravity
        fuel = (self.distance_from_sun - other_planet.distance_from_sun) / (self.gravity * other_planet.gravity)
        return fuel

# Create planets
earth = Planet('Earth', 24, 365, 1, 15, 9.8, 149.6)
mars = Planet('Mars', 24.6, 687, 2, -67, 3.7, 227.9)
jupiter = Planet('Jupiter', 9.9, 4333, 79, -150, 24.8, 778.3)

# Calculate time difference and fuel needed
time_diff = earth.calc_time_difference(mars)
fuel_needed = earth.calc_fuel_needed(mars)

print(f"Time difference between Earth and Mars: {time_diff}")
print(f"Fuel needed to travel from Earth to Mars: {fuel_needed}")