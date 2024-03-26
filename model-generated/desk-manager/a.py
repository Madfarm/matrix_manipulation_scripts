class Desk:
    def __init__(self, price, wood_type, desk_type):
        self.price = price
        self.wood_type = wood_type
        self.desk_type = desk_type

class DeskManager:
    def __init__(self):
        self.desks = []
        self.money = 0

    def add_desk(self, desk):
        self.desks.append(desk)

    def delete_desk(self, desk):
        self.desks.remove(desk)

    def edit_desk(self, desk, new_price, new_wood_type, new_desk_type):
        desk.price = new_price
        desk.wood_type = new_wood_type
        desk.desk_type = new_desk_type

    def search_desk(self, desk_type):
        return [desk for desk in self.desks if desk.desk_type == desk_type]

    def destroy_all(self):
        self.money += sum(desk.price for desk in self.desks)
        self.desks = []

# Demonstration
manager = DeskManager()

# Add desks
desk1 = Desk(100, 'Oak', 'Standing')
desk2 = Desk(200, 'Maple', 'Sitting')
manager.add_desk(desk1)
manager.add_desk(desk2)

# Delete a desk
manager.delete_desk(desk1)

# Edit a desk
manager.edit_desk(desk2, 300, 'Pine', 'Ergonomic')

# Search for desks
print(manager.search_desk('Standing'))  # Output: []
print(manager.search_desk('Ergonomic'))  # Output: [Desk(300, 'Pine', 'Ergonomic')]

# Destroy all desks
manager.destroy_all()
print(manager.money)  # Output: 300