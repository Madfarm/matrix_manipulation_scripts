# Define the characteristics of each planet
planets = {
    "Mercury": {"rotation_speed": 58.6, "size": 4879, "moons": 0, "distance_from_sun": 57.9},
    "Venus": {"rotation_speed": 243.0, "size": 12104, "moons": 0, "distance_from_sun": 108.2},
    "Earth": {"rotation_speed": 1677.0, "size": 12756, "moons": 1, "distance_from_sun": 149.6},
    "Mars": {"rotation_speed": 24.6, "size": 6794, "moons": 2, "distance_from_sun": 227.9},
    "Jupiter": {"rotation_speed": 9.9, "size": 142984, "moons": 79, "distance_from_sun": 778.3},
    "Saturn": {"rotation_speed": 10.7, "size": 120536, "moons": 82, "distance_from_sun": 1427},
    "Uranus": {"rotation_speed": 17.2, "size": 51118, "moons": 27, "distance_from_sun": 2871},
    "Neptune": {"rotation_speed": 16.1, "size": 49528, "moons": 14, "distance_from_sun": 4497.1},
}

# Define the musical notes corresponding to each planet's characteristics
notes = {
    "rotation_speed": {"low": "C", "medium": "E", "high": "G"},
    "size": {"small": "B", "medium": "D", "large": "F"},
    "moons": {"few": "A", "many": "C"},
    "distance_from_sun": {"close": "B", "medium": "D", "far": "F"},
}

# Function to map planet characteristics to musical notes
def map_to_notes(planet_data, notes_mapping):
    rotation_speed_note = notes["rotation_speed"]["low"] if planet_data["rotation_speed"] < 100 else notes["rotation_speed"]["medium"] if planet_data["rotation_speed"] < 500 else notes["rotation_speed"]["high"]
    size_note = notes["size"]["small"] if planet_data["size"] < 5000 else notes["size"]["medium"] if planet_data["size"] < 50000 else notes["size"]["large"]
    moons_note = notes["moons"]["few"] if planet_data["moons"] < 10 else notes["moons"]["many"]
    distance_from_sun_note = notes["distance_from_sun"]["close"] if planet_data["distance_from_sun"] < 100 else notes["distance_from_sun"]["medium"] if planet_data["distance_from_sun"] < 1000 else notes["distance_from_sun"]["far"]
    return rotation_speed_note, size_note, moons_note, distance_from_sun_note

# Generate the galactic symphony by mapping planet characteristics to musical notes
galactic_symphony = {}
for planet, planet_data in planets.items():
    rotation_speed_note, size_note, moons_note, distance_from_sun_note = map_to_notes(planet_data, notes)
    galactic_symphony[planet] = (rotation_speed_note, size_note, moons_note, distance_from_sun_note)

# Print the galactic symphony
for planet, symphony in galactic_symphony.items():
    print(f"{planet}: {symphony}")