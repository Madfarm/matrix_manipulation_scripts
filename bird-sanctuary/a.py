class BirdSanctuary:
    def __init__(self):
        self.phrases = []

    def record_phrase(self, phrase, timestamp):
        self.phrases.append((phrase, timestamp))

    def search_phrase(self, phrase):
        return [timestamp for p, timestamp in self.phrases if p == phrase]

# Create an instance of the BirdSanctuary class
sanctuary = BirdSanctuary()

# Record a phrase and its timestamp
sanctuary.record_phrase("Hello world!", "2022-01-01 08:00:00")

# Record another phrase and its timestamp
sanctuary.record_phrase("How are you?", "2022-01-01 08:05:00")

# Search for a phrase
timestamps = sanctuary.search_phrase("Hello world!")
print(timestamps)  # Output: ["2022-01-01 08:00:00"]

# Search for another phrase
timestamps = sanctuary.search_phrase("How are you?")
print(timestamps)  # Output: ["2022-01-01 08:05:00"]