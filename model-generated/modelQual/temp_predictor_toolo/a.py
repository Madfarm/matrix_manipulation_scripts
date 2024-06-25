def temp_predictor(previous_temps, month, date):
    # Assuming the temperature constantly increases from Nov to June and then constantly decreases from June to Nov
    # We will use the averages from June and Nov to predict the temperature of a future date
    if month == 'June':
        return previous_temps[0] + (date - 1) * (previous_temps[1] - previous_temps[0]) / 30
    elif month == 'November':
        return previous_temps[0] - (date - 1) * (previous_temps[1] - previous_temps[0]) / 30
    else:
        return "Invalid month"

# Demonstration of the tool
previous_temps = [76, 83]  # Average daily high temperatures in June
month = 'November'
date = 13
predicted_temp = temp_predictor(previous_temps, month, date)
print(f"The predicted temperature on October 13th is {predicted_temp}°F")