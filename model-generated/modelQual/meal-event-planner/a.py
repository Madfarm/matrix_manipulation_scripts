class MealPlanner:
    def __init__(self, entrees, snacks, beverages):
        self.entrees = entrees
        self.snacks = snacks
        self.beverages = beverages

    def plan_meals(self, attendees):
        meals = []
        for entree in self.entrees:
            for snack in self.snacks:
                for beverage in self.beverages:
                    meals.append((entree, snack, beverage))
        return meals[:attendees**2 + 1]

# Sample usage
entrees = ['Burger', 'Pizza', 'Salad']
snacks = ['Chips', 'Fries', 'Veggies']
beverages = ['Soda', 'Juice', 'Water']
planner = MealPlanner(entrees, snacks, beverages)
print(planner.plan_meals(3))