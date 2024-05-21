def find_meal(calories, protein):
    meals = [
        {"name": "Chicken Burrito", "calories": 500, "protein": 40},
        {"name": "Steak Bowl", "calories": 450, "protein": 35},
        {"name": "Veggie Salad", "calories": 300, "protein": 20},
        # Add more meals as needed
    ]

    for meal in meals:
        if abs(meal["calories"] - calories) / calories <= 0.25 and abs(meal["protein"] - protein) / protein <= 0.25:
            return meal["name"]

    return "No meal found within 25% of the given calories and protein."

# Example usage:
print(find_meal(400, 30))