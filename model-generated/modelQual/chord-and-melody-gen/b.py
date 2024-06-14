import random

def generate_chords_and_melodies(notes):
    assert len(notes) >= 3 and len(notes) <= 7, "The list of notes must contain between 3 and 7 notes."

    chords = {}
    melodies = {}

    for i in range(len(notes)):
        # Generate triads
        triad = [notes[i], notes[(i+1)%len(notes)], notes[(i+2)%len(notes)]]
        chords[f"Triad {i+1}"] = triad

        # Generate dyads
        dyad = [notes[i], notes[(i+1)%len(notes)]]
        melodies[f"Dyad {i+1}"] = dyad

    return chords, melodies

# Test the function
notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
chords, melodies = generate_chords_and_melodies(notes)
print("Chords:", chords)
print("Melodies:", melodies)