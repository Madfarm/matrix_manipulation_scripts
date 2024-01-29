import json

def adjust_recipe(original_ingredients, original_servings, new_servings):
  """Adjusts ingredient quantities for a new number of servings.

  Args:
    original_ingredients: A dictionary where keys are ingredient names and
      values are their original quantities (e.g., {"flour": "2 cups"}).
    original_servings: The number of servings the original recipe is for.
    new_servings: The desired number of servings for the adjusted recipe.

  Returns:
    A JSON string representing the adjusted recipe.
  """

  ratio = new_servings / original_servings

  new_ingredients = {}
  for ingredient, quantity in original_ingredients.items():
    amount, unit = quantity.strip().split(" ", 1)
    try:
      amount = float(amount)
    except ValueError:
      amount = 1
    new_amount = amount * ratio
    new_quantity = f"{new_amount:.2f} {unit}"
    new_ingredients[ingredient] = new_quantity

  adjusted_recipe = {
    "original_servings": original_servings,
    "new_servings": new_servings,
    "ingredients": new_ingredients
  }

  return json.dumps(adjusted_recipe, indent=2)  # Convert to JSON with indentation


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


print(adjust_recipe(original_ingredients, original_servings, new_servings))