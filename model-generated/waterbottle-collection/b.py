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

    def add_bottle(self, id, volume, color, spout_type):
        new_bottle = WaterBottle(id, volume, color, spout_type)
        self.bottles.append(new_bottle)

    def delete_bottle(self, id):
        self.bottles = [b for b in self.bottles if b.id != id]

    def search_bottle(self, id):
        for b in self.bottles:
            if b.id == id:
                return b
        return None

    def edit_bottle(self, id, volume=None, color=None, spout_type=None):
        bottle = self.search_bottle(id)
        if bottle:
            if volume:
                bottle.volume = volume
            if color:
                bottle.color = color
            if spout_type:
                bottle.spout_type = spout_type

    def sort_bottles(self):
        self.bottles.sort(key=lambda b: b.volume)

# Demonstration
collection = WaterBottleCollection()
collection.add_bottle(1, 500, "blue", "wide")
collection.add_bottle(2, 750, "green", "narrow")
collection.add_bottle(3, 1000, "red", "sport")

print("Bottles:")
print(collection.bottles)

collection.edit_bottle(2, volume=800)
collection.delete_bottle(1)

print("\nBottles after editing and deleting:")
print(collection.bottles)

print("\nSearching for bottle with id 3:")
print(collection.search_bottle(3))

collection.sort_bottles()
print("\nBottles after sorting:")
print(collection.bottles)