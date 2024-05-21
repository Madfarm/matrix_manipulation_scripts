def find_meal(calories, protein):
    # Define the menu options
    menu = {
        "Grilled Chicken": {"calories": 180, "protein": 32},
        "Steak": {"calories": 150, "protein": 25},
        "Sofritas": {"calories": 150, "protein": 8},
        "Fajita Veggies": {"calories": 20, "protein": 2},
        "Lettuce Blend": {"calories": 10, "protein": 1}
    }

    # Calculate the target calorie and protein ranges
    target_calories = calories * 0.75
    target_protein = protein * 0.75

    # Find the meal that is within the target ranges
    for option, nutrition in menu.items():
        if nutrition["calories"] >= target_calories and nutrition["protein"] >= target_protein:
            return option

    # If no meal is found, return None
    return None

# Test the function
print(find_meal(200, 30))