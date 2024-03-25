class WaterBottle:
    def __init__(self, id, volume, color, spout_type):
        self.id = id
        self.volume = volume
        self.color = color
        self.spout_type = spout_type

    def __repr__(self):
        return f'WaterBottle({self.id}, {self.volume}, "{self.color}", "{self.spout_type}")'


class WaterBottleCollection:
    def __init__(self):
        self.bottles = []

    def add_bottle(self, bottle):
        self.bottles.append(bottle)

    def delete_bottle(self, id):
        self.bottles = [b for b in self.bottles if b.id != id]

    def search_bottle(self, id):
        return [b for b in self.bottles if b.id == id]

    def edit_bottle(self, id, volume=None, color=None, spout_type=None):
        for b in self.bottles:
            if b.id == id:
                if volume:
                    b.volume = volume
                if color:
                    b.color = color
                if spout_type:
                    b.spout_type = spout_type

    def sort_bottles(self):
        self.bottles.sort(key=lambda x: x.volume)


# Demonstration
collection = WaterBottleCollection()
collection.add_bottle(WaterBottle(1, 500, "blue", "wide"))
collection.add_bottle(WaterBottle(2, 300, "green", "narrow"))
collection.add_bottle(WaterBottle(3, 700, "red", "sport"))

print("Bottles:", collection.bottles)

collection.delete_bottle(2)
print("After deleting a bottle:", collection.bottles)

print("Searching for bottle with id 1:", collection.search_bottle(1))

collection.edit_bottle(1, volume=500, color="black")
print("After editing a bottle:", collection.bottles)

collection.sort_bottles()
print("Bottles sorted by volume:", collection.bottles)