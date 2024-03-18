class Collection:
    def __init__(self):
        self.items = {}

    def add_item(self, name, item_id, condition, price):
        self.items[item_id] = {'name': name, 'condition': condition, 'price': price}

    def delete_item(self, item_id):
        if item_id in self.items:
            del self.items[item_id]

    def appraise_item(self, item_id):
        if item_id in self.items:
            item = self.items[item_id]
            # Assume condition deteriorates by 10% each time it's appraised
            item['condition'] *= 0.9
            return item['price'] * item['condition']

    def calculate_total_value(self):
        total_value = 0
        for item in self.items.values():
            total_value += item['price'] * item['condition']
        return total_value

# Demonstration
collection = Collection()
collection.add_item('Item1', 1, 1.0, 100)
collection.add_item('Item2', 2, 0.8, 150)
print(collection.calculate_total_value())  # Output: 230.0
print(collection.appraise_item(1))  # Output: 90.0
print(collection.calculate_total_value())  # Output: 217.0