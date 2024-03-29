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
        # Calculate the expected temperature based on the avg_temp and distance_from_sun
        if day > self.year_length:
            return "Invalid input: Day should be less than or equal to the year length."
        
        # Assuming that the temperature varies linearly with the distance from the sun
        # and the gravity of the planet
        temp_diff = self.avg_temp * (self.distance_from_sun ** (self.gravity / 10))
        daily_temp_diff = temp_diff / self.year_length
        expected_temp = self.avg_temp + daily_temp_diff * day
        return expected_temp
    
    def calculate_temp_difference(self, other_planet, day):
        # Calculate the temperature difference between two planets on a given day
        temp_diff = self.calculate_temp_on_day(day) - other_planet.calculate_temp_on_day(day)
        if temp_diff < 0:
            return f"The temperature is {abs(temp_diff)} degrees colder on {other_planet.name}"
        else:
            return f"The temperature is {temp_diff} degrees hotter on {other_planet.name}"

# Create two planet objects
earth = Planet("Earth", 24, 365, 1, 15, 9.8, 1)
mars = Planet("Mars", 24, 365, 2, 20, 3.7, 1.5)

# Calculate the temperature difference on a given day
print(earth.calculate_temp_difference(mars, 100))