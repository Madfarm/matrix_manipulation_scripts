class Pastry:
    def __init__(self, name, ingredients, baking_time, id):
        self.name = name
        self.ingredients = ingredients
        self.baking_time = baking_time
        self.id = id




class Kitchen:
    def __init__(self, ingredients_supply):
        self.ingredients_supply = ingredients_supply
        self.oven_time = 0

    def allocate_ingredients(self, pastry):
        for ingredient in pastry.ingredients:
            if self.ingredients_supply[ingredient] < 1:
                return False
            self.ingredients_supply[ingredient] -= 1
        return True

    def allocate_oven_time(self, pastry):
        if self.oven_time + pastry.baking_time > 100:  # assume 100 is the maximum oven time
            return False
        self.oven_time += pastry.baking_time
        return True
    

class Bakery:
    def __init__(self, kitchen, pastries):
        self.kitchen = kitchen
        self.pastries = pastries
        self.queue = []

    def add_pastry(self, pastry):
        if not self.kitchen.allocate_ingredients(pastry):
            print(f"Error: Not enough ingredients to bake {pastry.name}")
            return
        if not self.kitchen.allocate_oven_time(pastry):
            print(f"Error: Not enough oven time to bake {pastry.name}")
            return
        self.queue.append(pastry)

    def bake_next(self):
        if not self.queue:
            return None

        pastry = self.queue[0]
        print(pastry)
        if not self.kitchen.allocate_ingredients(pastry):
            print(f"Error: Ran out of ingredients for {pastry.name}")
            return None
        if not self.kitchen.allocate_oven_time(pastry):
            print(f"Error: Ran out of oven time for {pastry.name}")
            return None

        self.queue.pop(0)
        return pastry


pastries = [
    Pastry("Croissant", ["butter", "flour", "yeast"], 20, 1),
    Pastry("Tart", ["eggs", "sugar", "pastry_dough"], 30, 2),
    Pastry("Cake", ["flour", "sugar", "eggs"], 40, 3),
    Pastry("Cookie", ["butter", "sugar", "eggs"], 10, 4),
]

kitchen = Kitchen({"butter": 5, "flour": 10, "yeast": 3, "eggs": 4, "sugar": 6, "pastry_dough": 2})
bakery = Bakery(kitchen, pastries)

for pastry in pastries:
    bakery.add_pastry(pastry)
    # print(bakery.queue)

while True:
    pastry = bakery.bake_next()
    if pastry is None:
        break
    print(f"Baking {pastry.name} with ID {pastry.id}")