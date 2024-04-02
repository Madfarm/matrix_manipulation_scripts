class Banana:
    def __init__(self, color):
        self.color = color


    def check_ripeness(self):
        if self.color == "green":
            return "This banana is not ripe. It is edible, but it's not at its best."
        elif self.color == "yellow":
            return "This banana is ripe. It is perfectly edible and delicious!"
        elif self.color == "brown":
            return "This banana is ripe, but it's only good for baking."
        else:
            return "This banana's color is unknown. Please check it manually."


class BananaTracker:
    def __init__(self):
        self.bananas = []


    def add_banana(self, color):
        self.bananas.append(Banana(color))


    def check_banana(self, index):
        if index < 0 or index >= len(self.bananas):
            return "Invalid banana index. Please provide a valid index."
        return self.bananas[index].check_ripeness()


    def check_all_bananas(self):
        for i, banana in enumerate(self.bananas):
            print(f"Banana {i+1}: {banana.check_ripeness()}")


# create a tracker and add some bananas
tracker = BananaTracker()
tracker.add_banana("green")
tracker.add_banana("yellow")
tracker.add_banana("brown")


# check the ripeness of all bananas
tracker.check_all_bananas()


# check the ripeness of a specific banana
print(tracker.check_banana(0))