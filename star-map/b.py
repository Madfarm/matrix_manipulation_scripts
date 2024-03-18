class Star:
    def __init__(self, name, spectral_type, magnitude, x, y, z, planets=None):
        self.name = name
        self.spectral_type = spectral_type
        self.magnitude = magnitude
        self.x = x
        self.y = y
        self.z = z
        self.planets = planets if planets is not None else []

    def distance_to(self, other_star):
        return ((self.x - other_star.x)**2 + (self.y - other_star.y)**2 + (self.z - other_star.z)**2)**0.5

# Example usage:

# Create some stars
proxima_centauri = Star("Proxima Centauri", "M", -1.3, -0.016, 0, 0, ["Proxima b"])
sirius = Star("Sirius", "A", -1.46, 0, 0, 0)
alpheratz = Star("Alpheratz", "B", -2.06, 0.00139, 0.00235, 0.00054)

# Calculate distance between stars
distance_between_proxima_and_sirius = proxima_centauri.distance_to(sirius)
distance_between_proxima_and_alpheratz = proxima_centauri.distance_to(alpheratz)

print(f"Distance between Proxima Centauri and Sirius: {distance_between_proxima_and_sirius} parsecs")
print(f"Distance between Proxima Centauri and Alpheratz: {distance_between_proxima_and_alpheratz} parsecs")