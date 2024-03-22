import datetime

class BirdSanctuary:
    def __init__(self):
        self.phrases = {}

    def record_phrase(self, phrase):
        timestamp = str(datetime.datetime.now())
        if phrase not in self.phrases:
            self.phrases[phrase] = [timestamp]
        else:
            self.phrases[phrase].append(timestamp)

    def search_phrase(self, phrase):
        if phrase in self.phrases:
            return self.phrases[phrase]
        else:
            return []

sanctuary = BirdSanctuary()

# Record some phrases
sanctuary.record_phrase("Hello")
sanctuary.record_phrase("Goodbye")
sanctuary.record_phrase("Hello")

# Search for a phrase
print(sanctuary.search_phrase("Hello"))
print(sanctuary.search_phrase("Python"))