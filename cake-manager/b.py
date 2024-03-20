class Cake:
    def __init__(self, name, fluffiness, ingredients, flavor, days_until_expire):
        self.name = name
        self.fluffiness = fluffiness
        self.ingredients = ingredients
        self.flavor = flavor
        self.days_until_expire = days_until_expire

class CakeManager:
    def __init__(self):
        self.cakes = []

    def add_cake(self, cake):
        self.cakes.append(cake)

    def delete_cake(self, name):
        self.cakes = [cake for cake in self.cakes if cake.name != name]

    def delete_expired_cakes(self):
        self.cakes = [cake for cake in self.cakes if cake.days_until_expire > 0]

# Demonstration
cake1 = Cake("Chocolate", 5, ["flour", "sugar", "chocolate"], "chocolate", 5)
cake2 = Cake("Vanilla", 3, ["flour", "sugar", "milk"], "vanilla", 0)

manager = CakeManager()
manager.add_cake(cake1)
manager.add_cake(cake2)

print("Cakes before deletion:")
for cake in manager.cakes:
    print(cake.name)

manager.delete_expired_cakes()

print("\nCakes after deletion:")
for cake in manager.cakes:
    print(cake.name)