class PianoSongTracker:
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

# Demonstration
tracker = PianoSongTracker(5)
print(tracker.practice(["good", "mistake", "good", "good", "good"]))  # 4
print(tracker.practice(["good", "good", "good", "good", "good"]))  # 9
print(tracker.practice(["good", "good", "good", "good", "good"]))  # 14
print(tracker.practice(["good", "good", "good", "good", "good"]))  # 19
print(tracker.practice(["good", "good", "good", "good", "good"]))  # 24 
print(tracker.practice(["mistake", "mistake", "mistake", "mistake", "mistake"]))  # 9 
