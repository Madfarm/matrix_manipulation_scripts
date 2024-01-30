import random


# Helper function to check distance (more than 2 units)
def is_far_enough(loc1, loc2):
    return abs(loc1[0] - loc2[0]) > 2 or abs(loc1[1] - loc2[1]) > 2

# Helper function to check if moon is within range
def is_within_moon_range(loc1, loc2):
    return abs(loc1[0] - loc2[0]) <= 2 and abs(loc1[1] - loc2[1]) <= 2


class CelestialBody:
    def __init__(self, name, size, type):
        self.name = name
        self.size = size
        self.type = type
        self.location = self.generate_location()

    def generate_location(self):
        while True:
            x = random.randint(1, 100)
            y = random.randint(1, 100)
            if self.check_distance_constraints([x, y]):
                return [x, y]

    def __str__(self):
        return f"{self.name} ({self.type}, Size: {self.size}, Location: {self.location})"

class Star(CelestialBody):
    def __init__(self, name, size):
        super().__init__(name, size, "Star")

    def check_distance_constraints(self, location):
        # Check distances from other stars in the galaxy
        for star, _ in galaxy.star_systems:
            if star is not self and not is_far_enough(location, star.location):
                return False
        return True

class Planet(CelestialBody):
    def __init__(self, name, size, type, has_moons=False):
        super().__init__(name, size, type)
        self.moons = []
        self.has_moons = has_moons

    def check_distance_constraints(self, location):
        # Check distance from the parent star
        for star, planets in galaxy.star_systems:
            if star.name == self.star_name and not is_far_enough(location, star.location):
                return False
        # Check distances from other planets in the same star system
        for planet in planets:
            if planet is not self and not is_far_enough(location, planet.location):
                return False
        return True
    
    def add_moon(self, moon):
       self.moons.append(moon)
       self.has_moons = True

    def remove_moon(self, moon_name):
       for i, moon in enumerate(self.moons):
           if moon.name == moon_name:
               del self.moons[i]
               return
       print("Moon not found.")

    def __str__(self):
       moon_names = ", ".join([moon.name for moon in self.moons]) if self.moons else "None"
       return f"Planet {self.name}:\n" \
              f"  Size: {self.size}\n" \
              f"  Type: {self.type}\n" \
              f"  Moons: {moon_names}"

class Moon(CelestialBody):
    def __init__(self, name, size, planet):
        super().__init__(name, size, "Moon")
        self.planet = planet

    def generate_location(self):
        while True:
            x = self.planet.location[0] + random.randint(-2, 2)
            y = self.planet.location[1] + random.randint(-2, 2)
            location = [x, y]
            if is_within_moon_range(location, self.planet.location):
                return location
            

class Galaxy:
   def __init__(self, name):
       self.name = name
       self.star_systems = []

   def add_star_system(self, star, planets=[]):
       self.star_systems.append((star, planets))

   def remove_star_system(self, star_name):
       for i, (star, planets) in enumerate(self.star_systems):
           if star.name == star_name:
               del self.star_systems[i]
               return
       print("Star system not found.")

   def add_planet(self, star_name, planet):
       for star, planets in self.star_systems:
           if star.name == star_name:
               planets.append(planet)
               return
       print("Star system not found.")

   def remove_planet(self, star_name, planet_name):
       for star, planets in self.star_systems:
           if star.name == star_name:
               for i, planet in enumerate(planets):
                   if planet.name == planet_name:
                       del planets[i]
                       return
               print("Planet not found.")

   def __str__(self):
       output = f"Galaxy {self.name}:\n"
       for star, planets in self.star_systems:
           output += f"  Star: {star.name}\n"
           for planet in planets:
               output += f"    {planet}\n"
       return output
# --- Example usage ---

galaxy = Galaxy("Milky Way")

star1 = Star("Sun", 100)
planet1 = Planet("Earth", 10, "Rocky")
planet2 = Planet("Mars", 8, "Rocky")
moon1 = Moon("Luna", 2)
planet1.add_moon(moon1)

star2 = Star("Alpha Centauri", 90)
planet3 = Planet("Proxima b", 12, "Rocky", has_moons=True)
moon2 = Moon("Proxima c", 3)
planet3.add_moon(moon2)

galaxy.add_star_system(star1, [planet1, planet2])
galaxy.add_star_system(star2, [planet3])

# Add a new planet to the Sun's system
planet4 = Planet("Jupiter", 120, "Gas")
galaxy.add_planet("Sun", planet4)

# Remove Mars
galaxy.remove_planet("Sun", "Mars")

# Remove Proxima c moon
planet3.remove_moon("Proxima c")
print(galaxy)
