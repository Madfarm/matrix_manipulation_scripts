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
    # Generate the time signature
    time_signature = f"{num_beats}/{note_value}"
    return time_signature

# Define a function to generate a random tempo
def generate_tempo():
    # Select a random tempo range (slow, moderate, fast)
    tempo_range = random.choice(["slow", "moderate", "fast"])
    # Select a random tempo value within the range
    tempo_value = random.uniform(30, 120)
    # Generate the tempo marking
    tempo_marking = {
        "slow": f"Largo ({tempo_value})",
        "moderate": f"Moderato ({tempo_value})",
        "fast": f"Allegro ({tempo_value})"
    }[tempo_range]
    return tempo_marking

# Define a function to generate a random melody
def generate_melody(key_signature, time_signature):
    # Define a scale for the key signature
    scale = ["A", "B", "C", "D", "E", "F", "G"]
    # Select a random starting note
    starting_note = random.choice(scale)
    # Generate the melody
    melody = []
    for i in range(16):  # 16 notes per melody
        note = starting_note
        while note == starting_note:
            note = random.choice(scale)
        melody.append(note)
    return melody

# Define a function to generate a symphony
def generate_symphony():
    # Generate a unique symphony code
    symphony_code = "".join([random.choice(["A", "B", "C", "D", "E", "F", "G"]) for _ in range(3)])
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