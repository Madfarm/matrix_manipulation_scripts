def check_croissant(oven_temperature, butter_content, yeast_fermentation, dough_resting_time, rolling_and_folding, temperature_control, humidity):
    if oven_temperature < 400 or oven_temperature > 425:
        return "Oven temperature is not within the correct range. It should be between 400°F and 425°F."
    if butter_content < 30 or butter_content > 40:
        return "Butter content is not within the correct range. It should be between 30% and 40%."
    if yeast_fermentation != "active":
        return "Yeast fermentation is not active. Make sure yeast is fresh and at room temperature."
    if dough_resting_time < 1 or dough_resting_time > 2:
        return "Dough resting time is not within the correct range. It should be between 1 and 2 hours."
    if rolling_and_folding != "gentle":
        return "Rolling and folding is not gentle. Make sure to handle the dough gently to avoid developing gluten."
    if temperature_control != "stable":
        return "Temperature control is not stable. Make sure the oven temperature is consistent throughout the baking process."
    if humidity != "low":
        return "Humidity is not low. Make sure the environment is dry and not humid."

    return "Your croissant will turn out great!"

# Test the function
print(check_croissant(410, 35, "active", 1.5, "gentle", "stable", "low"))