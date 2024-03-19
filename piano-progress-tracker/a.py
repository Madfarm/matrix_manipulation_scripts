class PianoTracker:
    def __init__(self, num_of_notes):
        self.num_of_notes = num_of_notes
        self.progress = 0

    def practice(self, notes):
        if len(notes) != self.num_of_notes:
            return "wrong song!"

        for note in notes:
            if note == "good":
                self.progress = min(self.progress + 1, 100)
            elif note == "mistake":
                self.progress = max(self.progress - 3, 1)

        return self.progress

# Create an instance of the PianoTracker class
tracker = PianoTracker(5)

# Practice the song
print(tracker.practice(["good", "mistake", "good", "mistake", "good"]))  # Output: 3
print(tracker.practice(["good", "mistake", "good", "mistake", "good"]))  # Output: 6
print(tracker.practice(["good", "mistake", "good", "mistake", "good"]))  # Output: 9
print(tracker.practice(["good", "mistake", "good", "mistake", "good"]))  # Output: 12
print(tracker.practice(["good", "mistake", "good", "mistake", "good"]))  # Output: 15

# Try to practice the wrong song
print(tracker.practice(["good", "good", "good", "good", "good", "good"]))  # Output: "wrong song!"