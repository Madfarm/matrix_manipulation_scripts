class Collection:
    def __init__(self):
        self.items = {}

    def add_item(self, id, name, condition=100, price=0):
        self.items[id] = {'name': name, 'condition': condition, 'price': price}

    def delete_item(self, id):
        if id in self.items:
            del self.items[id]
        else:
            print("Item not found in collection")

    def appraise_item(self, id):
        if id in self.items:
            condition = self.items[id]['condition']
            if condition > 0:
                condition -= 10
                self.items[id]['condition'] = condition
                self.items[id]['price']= self.items[id]['price'] * (condition / 100)
                return self.items[id]['price']
            else:
                print("Item's condition is already at 0")
        else:
            print("Item not found in collection")

    def calculate_total_value(self):
        total_value = 0
        for item in self.items.values():
            total_value += item['price']
        return total_value

# Demonstration
collection = Collection()
collection.add_item(1, 'Item 1', 80, 1000)
collection.add_item(2, 'Item 2', 60, 500)
collection.add_item(3, 'Item 3', 90, 800)
print(collection.calculate_total_value())  # Output: 2300
collection.appraise_item(2)
print(collection.calculate_total_value())  # Output: 2050.0
collection.delete_item(3)
print(collection.calculate_total_value())  # Output: 1250.0