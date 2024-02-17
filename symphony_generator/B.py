import random

# Define a function to generate a random key signature
def generate_key_signature():
    # Select a random major or minor key
    key_type = random.choice(["major", "minor"])
    # Select a random key (A-G)
    key_letter = random.choice(["A", "B", "C", "D", "E", "F", "G"])
    # Determine the number of sharps or flats
    if key_type == "major":
        num_accidentals = random.randint(0, 3)
    else:
        num_accidentals = random.randint(1, 4)
    # Generate the key signature
    key_signature = []
    for i in range(num_accidentals):
        if random.randint(0, 1) == 0:
            key_signature.append("#")
        else:
            key_signature.append("b")
    key_signature.append(key_letter)
    return "".join(key_signature)

# Define a function to generate a random time signature
def generate_time_signature():
    # Select a random number of beats (2-5)
    num_beats = random.randint(2, 5)
    # Select a random note value (whole, half, quarter, etc.)
    note_value = random.choice(["w", "h", "q", "e", "s"])
    # Convert note value to number
    if note_value == "w":
        num_note_value = 4
    elif note_value == "h":
        num_note_value = 2
    elif note_value == "q":
        num_note_value = 1
    elif note_value == "e":
        num_note_value = 0.5
    elif note_value == "s":
        num_note_value = 0.25
    # Generate the time signature
    time_signature = f"{num_beats}/{num_note_value}"
    return time_signature

# Define a function to generate a random symphony code
def generate_symphony_code():
    # Generate 12 random characters in groups of 4 separated by hyphens
    symphony_code = []
    for i in range(3):
        symphony_code.append("".join([random.choice(["A", "B", "C", "D", "E", "F", "G"]) for _ in range(4)]))
        symphony_code.append("-")
    symphony_code.pop(-1)  # Remove last hyphen
    return "".join(symphony_code)

# Define a function to generate a symphony
def generate_symphony():
    # Generate a unique symphony code
    symphony_code = generate_symphony_code()
    # Generate four movements
    movements = []
    for i in range(4):
        # Generate a time signature, key signature, and tempo for the movement
        time_signature = generate_time_signature()
        key_signature = generate_key_signature()
        tempo_marking = generate_tempo()
        # Generate a melody for the movement
        melody = generate_melody(key_signature, time_signature)
        # Add the movement to the symphony
        movements.append((time_signature, key_signature, tempo_marking, melody))
    # Return the symphony
    return symphony_code, movements

# Generate a symphony
symphony_code, movements = generate_symphony()

# Print the symphony
print(f"Symphony Code: {symphony_code}")
for i, movement in enumerate(movements):
    print(f"Movement {i+1}:")
    print(f"Time Signature: {movement[0]}")
    print(f"Key Signature: {movement[1]}")
    print(f"Tempo: {movement[2]}")
    print(f"Melody: {', '.join(movement[3])}")
    print()