class MealPlanner:
    def __init__(self):
        self.entrees = ['Grilled Chicken', 'Baked Salmon', 'Vegetarian Quinoa Bowl']
        self.snacks = ['Chips and Dip', 'Veggie Sticks with Hummus', 'Fresh Fruit Salad']
        self.beverages = ['Soft Drinks', 'Iced Tea', 'Fresh Lemonade']

    def plan_meals(self, num_attendees):
        meal_combinations = []
        for entree in self.entrees:
            for snack in self.snacks:
                for beverage in self.beverages:
                    meal_combinations.append((entree, snack, beverage))
        return meal_combinations[:num_attendees**2 + 1]

meal_planner = MealPlanner()
meal_combinations = meal_planner.plan_meals(3)
for i, meal in enumerate(meal_combinations):
    print(f"Meal Combination {i+1}: {meal[0]}, {meal[1]}, {meal[2]}")
