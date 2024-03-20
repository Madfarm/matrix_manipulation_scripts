class Cake:
    def __init__(self, name, fluffiness, ingredients, flavor, days_until_expire):
        self.name = name
        self.fluffiness = fluffiness
        self.ingredients = ingredients
        self.flavor = flavor
        self.days_until_expire = days_until_expire

class CakeList:
    def __init__(self):
        self.cakes = []

    def add_cake(self, cake):
        self.cakes.append(cake)

    def delete_cake(self, name):
        self.cakes = [cake for cake in self.cakes if cake.name != name]

    def check_expired(self):
        self.cakes = [cake for cake in self.cakes if cake.days_until_expire > 0]

    def filter_by_ingredients(self, ingredient):
        return [cake for cake in self.cakes if ingredient in cake.ingredients]

    def sort_by_expiration_days(self):
        self.cakes.sort(key=lambda cake: cake.days_until_expire)

# Demonstration
cake1 = Cake("Chocolate", 5, ["flour", "sugar", "chocolate"], "delicious", 2)
cake2 = Cake("Vanilla", 3, ["flour", "sugar", "milk"], "yummy", 0)
cake3 = Cake("Carrot", 4, ["flour", "sugar", "carrots"], "nice", 1)

cake_list = CakeList()
cake_list.add_cake(cake1)
cake_list.add_cake(cake2)
cake_list.add_cake(cake3)

print("Cakes with flour:")
for cake in cake_list.filter_by_ingredients("milk"):
    print(cake.name)

print("\nCakes sorted by expiration days:")
cake_list.sort_by_expiration_days()
for cake in cake_list.cakes:
    print(cake.name, cake.days_until_expire)

