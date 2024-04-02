class Banana:
    def __init__(self, name, ripeness):
        self.name = name
        self.ripeness = ripeness


class BananaTracker:
    def __init__(self):
        self.bananas = {}


    def add_banana(self, banana):
        self.bananas[banana.name] = banana


    def check_banana(self, name):
        if name in self.bananas:
            return self.bananas[name].ripeness
        else:
            return "Banana not found"


# Create a banana tracker
tracker = BananaTracker()


# Create some bananas
banana1 = Banana("banana1", "green")
banana2 = Banana("banana2", "yellow")
banana3 = Banana("banana3", "brown")


# Add the bananas to the tracker
tracker.add_banana(banana1)
tracker.add_banana(banana2)
tracker.add_banana(banana3)


# Check the ripeness of a banana
print(tracker.check_banana("banana1"))  # Output: green
print(tracker.check_banana("banana2"))  # Output: yellow
print(tracker.check_banana("banana3"))  # Output: brown
print(tracker.check_banana("banana4"))  # Output: Banana not found