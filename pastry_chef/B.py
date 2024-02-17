import heapq

class Pastry:
    def __init__(self, name, ingredients, baking_time, id_num):
        self.name = name
        self.ingredients = ingredients
        self.baking_time = baking_time
        self.id_num = id_num

class Oven:
    def __init__(self, max_ingredients):
        self.max_ingredients = max_ingredients
        self.ingredient_supplies = {}
        self.pastries_queue = []

    def add_pastry(self, pastry):
        self.pastries_queue.append(pastry)
        for ingredient in pastry.ingredients:
            if ingredient not in self.ingredient_supplies:
                self.ingredient_supplies[ingredient] = 0
            self.ingredient_supplies[ingredient] -= 1

    def bake_next(self):
        # Prioritize pastry with fewest unique ingredients
        pastry = min(self.pastries_queue, key=lambda p: len(p.ingredients))

        # Check if ingredient supplies are sufficient
        if any(self.ingredient_supplies[ingredient] < 0 for ingredient in pastry.ingredients):
            return None

        # Bake the pastry and update ingredient supplies
        self.ingredient_supplies[pastry.ingredients[0]] += 1  # assume first ingredient is the most limited
        return pastry

def main():
    # Initialize oven with limited supplies
    oven = Oven(max_ingredients=5)
    oven.ingredient_supplies = {'flour': 5, 'sugar': 10, 'butter': 8, 'eggs': 4, 'chocolate': 3}

    # Define pastries with multiple ingredients
    pastries = [
        Pastry(' Croissant', ['flour', 'butter', 'eggs'], 20, 1),
        Pastry(' Mille-Feuille', ['pastry_dough', 'pastry_cream', 'chocolate'], 30, 2),
        Pastry(' Éclairs', ['pastry_dough', 'cream', 'chocolate'], 25, 3),
        Pastry(' Macarons', ['ground_almonds', 'sugar', 'egg_whites'], 15, 4),
        Pastry(' Brownies', ['chocolate', 'sugar', 'eggs'], 25, 5),
    ]

    # Add pastries to oven's queue
    for pastry in pastries:
        oven.add_pastry(pastry)

    # Bake pastries one by one
    while oven.pastries_queue:
        pastry = oven.bake_next()
        if pastry:
            print(f"Baked {pastry.name} with id {pastry.id_num} using {', '.join(pastry.ingredients)}")

if __name__ == "__main__":
    main()