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

# Demonstration
cake1 = Cake("Chocolate", 5, ["flour", "sugar", "chocolate"], "delicious", 2)
cake2 = Cake("Vanilla", 3, ["flour", "sugar", "milk"], "yummy", 0)

cake_list = CakeList()
cake_list.add_cake(cake1)
cake_list.add_cake(cake2)

print("Cakes before check:", [cake.name for cake in cake_list.cakes])
cake_list.check_expired()
print("Cakes after check:", [cake.name for cake in cake_list.cakes])

cake_list.delete_cake("Chocolate")
print("Cakes after deleting Chocolate:", [cake.name for cake in cake_list.cakes])