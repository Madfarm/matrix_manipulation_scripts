class Desk:
    def __init__(self, price, wood_type, desk_type):
        self.price = price
        self.wood_type = wood_type
        self.desk_type = desk_type

class DeskManager:
    def __init__(self):
        self.desks = []
        self.money = 0

    def add_desk(self, price, wood_type, desk_type):
        new_desk = Desk(price, wood_type, desk_type)
        self.desks.append(new_desk)

    def delete_desk(self, desk_type):
        self.desks = [desk for desk in self.desks if desk.desk_type != desk_type]

    def edit_desk(self, desk_type, new_price, new_wood_type, new_desk_type):
        for desk in self.desks:
            if desk.desk_type == desk_type:
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
manager.add_desk(100, 'Oak', 'Modern')
manager.add_desk(150, 'Walnut', 'Classic')
manager.add_desk(200, 'Pine', 'Contemporary')
print(manager.desks)

manager.edit_desk('Modern', 120, 'Ash', 'Minimalist')
print(manager.desks)

manager.delete_desk('Classic')
print(manager.desks)

print(manager.search_desk('Contemporary'))

manager.destroy_all()
print(manager.desks)
print(manager.money)