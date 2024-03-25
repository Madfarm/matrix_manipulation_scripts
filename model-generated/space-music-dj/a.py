import math

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

# Define the musical notes
notes = ["C", "D", "E", "F", "G", "A", "B"]

# Function to convert a number to a musical note
def number_to_note(number):
    index = int(number) % len(notes)
    return notes[index]

# Generate the symphony for each planet
for planet, characteristics in planets.items():
    rotation_note = number_to_note(characteristics["rotation_speed"])
    size_note = number_to_note(characteristics["size"])
    moons_note = number_to_note(characteristics["moons"])
    distance_note = number_to_note(characteristics["distance_from_sun"])

    print(f"{planet}: {rotation_note} {size_note} {moons_note} {distance_note}")