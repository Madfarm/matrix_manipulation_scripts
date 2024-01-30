import random

class CelestialBody:
    def __init__(self, name, size, type):
        self.name = name
        self.size = size
        self.type = type
        self.location = self.generate_location()

    def generate_location(self):
        return [random.randint(1, 100), random.randint(1, 100)]

    def distance_to(self, other):
        dx = abs(self.location[0] - other.location[0])
        dy = abs(self.location[1] - other.location[1])
        return (dx ** 2 + dy ** 2) ** 0.5  # Calculate distance

    def __str__(self):
        return f"{self.type}: {self.name} (Size: {self.size}, Location: {self.location})"

class Star(CelestialBody):
    def __init__(self, name, size):
        super().__init__(name, size, "Star")

    def generate_location(self):
        while True:  # Ensure stars are sufficiently apart
            location = super().generate_location()
            valid = all(self.distance_to(star) > 2 for star, _ in galaxy.star_systems)
            if valid:
                return location

class Planet(CelestialBody):
    def __init__(self, name, size, type, has_moons=False):
        super().__init__(name, size, type)
        self.moons = []
        self.has_moons = has_moons

    def generate_location(self):
        for star, planets in galaxy.star_systems:
            if self in planets:  # Find the parent star
                while True:
                    location = [
                        star.location[0] + random.randint(-2, 2),
                        star.location[1] + random.randint(-2, 2)
                    ]
                    # Ensure distance from star and other planets
                    if all(self.distance_to(other) > 2 for other in planets if other is not self):
                        return location

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
        moon_str = "\n  Moons: " + ", ".join([m.name for m in self.moons]) if self.moons else ""
        return f"Planet: {self.name} (Size: {self.size}, Type: {self.type}){moon_str}"


class Moon(CelestialBody):
    def __init__(self, name, size, planet):
        super().__init__(name, size, "Moon")
        self.planet = planet
        self.location = self.generate_location()  # Set location based on parent planet

    def generate_location(self):
        return [self.planet.location[0] + random.randint(-2, 2), self.planet.location[1] + random.randint(-2, 2)]

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
        output = f"Galaxy: {self.name}\n"
        for star, planets in self.star_systems:
            output += f"Star System: {star.name}\n"
            for planet in planets:
                output += f"  {planet}\n"
        return output

# --- Example usage ---

galaxy = Galaxy("Milky Way")

star1 = Star("Sun", 100)
planet1 = Planet("Earth", 10, "Rocky")
planet2 = Planet("Mars", 8, "Rocky")
moon1 = Moon("Luna", 2, planet1)
planet1.add_moon(moon1)

star2 = Star("Alpha Centauri", 90)
planet3 = Planet("Proxima b", 12, "Rocky", has_moons=True)
moon2 = Moon("Proxima c", 3, planet3)
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