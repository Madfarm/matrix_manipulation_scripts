def generate_chords_and_melodies(notes):
    assert len(notes) >= 3 and len(notes) <= 7, "The list of notes must contain between 3 and 7 notes."
    assert all(isinstance(note, str) for note in notes), "All notes must be strings."
    assert all(note.isalpha() for note in notes), "All notes must be alphabetic."

    chords = {
        "triads": [tuple(sorted([notes[i], notes[j], notes[k]])) for i in range(len(notes)) for j in range(i+1, len(notes)) for k in range(j+1, len(notes))],
        "dyads": [tuple(sorted([notes[i], notes[j]])) for i in range(len(notes)) for j in range(i+1, len(notes))]
    }

    melodies = {
        "ascending": tuple(sorted(notes)),
        "descending": tuple(sorted(notes, reverse=True))
    }

    return {"chords": chords, "melodies": melodies}

# Test the function
print(generate_chords_and_melodies(["C", "D", "E", "F", "G", "A", "B"]))