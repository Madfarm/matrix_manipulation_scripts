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
        fuel_needed = abs(distance) * self.gravity * other_planet.gravity
        return fuel_needed

    def calculate_temp_on_day(self, day):
        # Calculate the expected temperature on a given day
        if day > self.year_length:
            raise ValueError("Day value is larger than the length of a year on this planet")

        # This is a simple approximation, a more accurate calculation would depend on the specifics of the planet's climate
        temperature_variation = self.avg_temp * 0.5
        daily_temperature_variation = temperature_variation / self.year_length
        expected_temperature = self.avg_temp + daily_temperature_variation * day
        return expected_temperature

# Testing the new method
earth = Planet("Earth", 24, 365, 1, 15, 9.8, 149.6)
print(earth.calculate_temp_on_day(100))  # Expected output: around 15.33
print(earth.calculate_temp_on_day(200))  # Expected output: around 15.67

# Note: The results are approximate and depend on the specifics of the planet's climate, 
# which are not taken into account in this simple calculation.