import math

class Star:
    def __init__(self, name, spectral_type, magnitude, x, y, z, planets=None):
        self.name = name
        self.spectral_type = spectral_type
        self.magnitude = magnitude
        self.x = x
        self.y = y
        self.z = z
        self.planets = planets if planets else []

    def distance_to(self, other_star):
        return math.sqrt((self.x - other_star.x)**2 + (self.y - other_star.y)**2 + (self.z - other_star.z)**2)

# Create some stars
star1 = Star("Sun", "G", -26.74, 0, 0, 0, ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"])
star2 = Star("Betelgeuse", "M", 0.72, 188.5, 712.4, 0)
star3 = Star("Vega", "A", 0.03, 25.0, 60.0, 0)

# Calculate and print distances
print(f"Distance from {star1.name} to {star2.name}: {star1.distance_to(star2)} light years")
print(f"Distance from {star1.name} to {star3.name}: {star1.distance_to(star3)} light years")
print(f"Distance from {star2.name} to {star3.name}: {star2.distance_to(star3)} light years")