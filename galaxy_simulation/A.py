import random

class CelestialBody:
    def __init__(self, name, size, type):
        self.name = name
        self.size = size
        self.type = type

class Star(CelestialBody):
    def __init__(self, name, size):
        super().__init__(name, size, "Star")

class Planet(CelestialBody):
    def __init__(self, name, size, type, has_moons=False):
        super().__init__(name, size, type)
        self.moons = []
        self.has_moons = has_moons

    def add_moon(self, moon):
        self.moons.append(moon)
        self.has_moons = True

    def remove_moon(self, moon_name):
        for i, moon in enumerate(self.moons):
            if moon.name == moon_name:
                del self.moons[i]
                return
        print("Moon not found.")

class Moon(CelestialBody):
    def __init__(self, name, size):
        super().__init__(name, size, "Moon")

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
galaxy.remove_moon("Proxima b", "Proxima c")
