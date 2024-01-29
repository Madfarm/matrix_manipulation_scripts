import json

def adjust_recipe(original_ingredients, original_servings, new_servings):
 """Adjusts ingredient quantities for a new number of servings.

 Args:
   original_ingredients: A dictionary where keys are ingredient names and
     values are their original quantities (e.g., {"flour": "2 cups"}).
   original_servings: The number of servings the original recipe is for.
   new_servings: The desired number of servings for the adjusted recipe.

 Returns:
   A dictionary with the same keys as original_ingredients, but with
   quantities adjusted for the new_servings.
 """

 ratio = new_servings / original_servings

 new_ingredients = {}
 for ingredient, quantity in original_ingredients.items():
   # Split quantity into numerical part and unit (e.g., "2 cups" -> 2, "cups")
   if " " in quantity:
     amount, unit = quantity.strip().split(" ", 1)
   else:
     amount, unit = quantity, ""
   try:
     amount = float(amount)  # Convert amount to a number
   except ValueError:
     amount = 1  # If no numerical part, assume quantity 1

   new_amount = amount * ratio
   new_quantity = f"{new_amount:.2f} {unit}".strip()  # Format with 2 decimal places
   new_ingredients[ingredient] = new_quantity

 return new_ingredients

# Get recipe details from the user
original_ingredients = {}
while True:
 ingredient = input("Enter ingredient name (or type 'done' to finish): ")
 if ingredient.lower() == "done":
   break
 quantity = input("Enter quantity for {}: ".format(ingredient))
 original_ingredients[ingredient] = quantity

original_servings = int(input("Original recipe serves: "))
new_servings = int(input("How many servings do you want? "))
# Calculate adjusted recipe
new_recipe = adjust_recipe(original_ingredients, original_servings, new_servings)

# Convert recipe to JSON 
recipe_json = json.dumps(new_recipe)

# Print the JSON output
print("\nAdjusted recipe (JSON):")
print(recipe_json)