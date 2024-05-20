def check_croissant(oven_temperature, butter_content, yeast_activity, dough_resting_time, rolling_and_folding, humidity):
    # Check oven temperature
    if oven_temperature < 400 or oven_temperature > 425:
        return "Oven temperature is not correct. It should be between 400°F and 425°F."

    # Check butter content
    if butter_content < 30 or butter_content > 40:
        return "Butter content is not correct. It should be between 30% and 40%."

    # Check yeast activity
    if yeast_activity < 0.5 or yeast_activity > 1.5:
        return "Yeast activity is not correct. It should be between 0.5 and 1.5."

    # Check dough resting time
    if dough_resting_time < 30 or dough_resting_time > 60:
        return "Dough resting time is not correct. It should be between 30 minutes and 1 hour."

    # Check rolling and folding
    if rolling_and_folding < 3 or rolling_and_folding > 5:
        return "Rolling and folding is not correct. It should be between 3 and 5 times."

    # Check humidity
    if humidity < 50 or humidity > 70:
        return "Humidity is not correct. It should be between 50% and 70%."

    # If all checks pass, return success message
    return "Your croissant will turn out great!"

# Example usage:
print(check_croissant(410, 35, 1.2, 45, 4, 60))