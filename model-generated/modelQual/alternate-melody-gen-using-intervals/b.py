def generate_alternate_melodies(melody):
    # Validate input
    assert isinstance(melody, list), "Input must be a list of notes"
    for note in melody:
        assert isinstance(note, str) and note.isalpha(), "Each note must be a string"
        assert len(note) == 1, "Each note must be a single character"
        assert note.upper() in 'ABCDEFG', "Each note must be a valid music pitch (A-G)"

    # Define intervals
    intervals = [2, 3, 5, 7, 11]  # Major 2nd, minor 3rd, perfect 5th, major 7th, perfect 11th

    # Generate alternate melodies
    alternate_melodies = []
    for interval in intervals:
        alternate_melody = []
        for note in melody:
            # Calculate new note using interval
            new_note = chr((ord(note) - ord('A') + interval) % 7 + ord('A'))
            alternate_melody.append(new_note)
        alternate_melodies.append(alternate_melody)

    return alternate_melodies

# Test the function
melody = ['B','E','A','D','A','E']
print(generate_alternate_melodies(melody))