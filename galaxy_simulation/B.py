import random

class CelestialBody:
    def __init__(self, name, size):
        self.name = name
        self.size = size

class Star(CelestialBody):
    pass

class Planet(CelestialBody):
    def __init__(self, name, size):
        super().__init__(name, size)
        self.moons = []

    def add_moon(self, moon):
        self.moons.append(moon)

    def remove_moon(self, moon_name):
        for moon in self.moons:
            if moon.name == moon_name:
                self.moons.remove(moon)
                return
        print(f"Moon with name '{moon_name}' not found.")

class Moon(CelestialBody):
    pass

class Galaxy:
    def __init__(self):
        self.stars = []

    def add_star(self, star):
        self.stars.append(star)

    def remove_star(self, star_name):
        for star in self.stars:
            if star.name == star_name:
                self.stars.remove(star)
                return
        print(f"Star with name '{star_name}' not found.")

    def find_star(self, star_name):
        for star in self.stars:
            if star.name == star_name:
                return star
        return None

# Example usage
my_galaxy = Galaxy()
sun = Star("Sun", 100) 
earth = Planet("Earth", 10) 
our_moon = Moon("Moon", 1)
other_moon = Moon("Other Moon", 1)

earth.add_moon(our_moon)
earth.add_moon(other_moon)
my_galaxy.add_star(sun)
earth.remove_moon("Other Moon")
