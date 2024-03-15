class DietTracker:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight
        self.calories = 0
        self.carbs = 0
        self.fat = 0
        self.protein = 0
        self.sugar = 0

    def add_food(self, calories, carbs, fat, protein, sugar):
        self.calories += calories
        self.carbs += carbs
        self.fat += fat
        self.protein += protein
        self.sugar += sugar

    def calculate_recommended_calories(self):
        return 66 + (13.7 * self.weight) + (5 * self.height) - 6.8 * 30

    def display_totals(self):
        print(f"Total Calories: {self.calories}")
        print(f"Total Carbs: {self.carbs} grams")
        print(f"Total Fat: {self.fat} grams")
        print(f"Total Protein: {self.protein} grams")
        print(f"Total Sugar: {self.sugar} grams")


# Demonstration
tracker = DietTracker(175, 65)  # height in cm, weight in kg
tracker.add_food(500, 60, 30, 50, 20)  # calories, carbs, fat, protein, sugar
tracker.add_food(300, 30, 20, 30, 10)  # calories, carbs, fat, protein, sugar
tracker.display_totals()
print(f"Recommended Calories: {tracker.calculate_recommended_calories()}")