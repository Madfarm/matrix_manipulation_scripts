class DietTracker:
    def __init__(self, name, height, weight):
        self.name = name
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
        # The Harris-Benedict Equation is used to estimate daily calorie needs.
        # It is based on sex, age, weight, and height.
        if self.name.lower() == 'male':
            return 66 + (6.2 * self.weight) + (12.7 * self.height) - (6.8 * self.age)
        else:
            return 655 + (4.35 * self.weight) + (4.7 * self.height) - (4.7 * self.age)

    def display_totals(self):
        print(f"Daily Totals for {self.name}:")
        print(f"Calories: {self.calories}")
        print(f"Carbs: {self.carbs}")
        print(f"Fat: {self.fat}")
        print(f"Protein: {self.protein}")
        print(f"Sugar: {self.sugar}")

    def display_recommended_calories(self):
        print(f"Recommended Calorie Intake for {self.name}: {self.calculate_recommended_calories()}")


# Example usage:
diet_tracker = DietTracker("John", 180, 70)  # height in cm, weight in kg
diet_tracker.add_food(500, 60, 30, 50, 20)
diet_tracker.add_food(1000, 120, 60, 80, 40)
diet_tracker.display_totals()
diet_tracker.display_recommended_calories()