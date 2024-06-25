from datetime import datetime
def temp_predictor(prev_temps, predict_date):
    # Function to calculate linear interpolation
    def linear_interpolate(x, x0, x1, y0, y1):
        return y0 + (y1 - y0) * ((x - x0) / (x1 - x0))
    
    # Predict temperature for the given date
    if predict_date.month <= 5:  # Months 1 to 5: Increasing towards June
        predicted_temp = linear_interpolate(predict_date.month,
                                            1, 6, 
                                            prev_temps["nov"][0], prev_temps["jun"][1])
    else:  # Months 6 to 11: Decreasing towards November
        predicted_temp = linear_interpolate(predict_date.month,
                                            6, 11, 
                                            prev_temps["nov"][1], prev_temps["jun"][0])
        
    return predicted_temp

# Date to predict
predict_date = datetime(year=2024, month=10, day=13)
prev_temps = {"jun": (76,83), "nov": (49,59)}

# Predict the temperature
predicted_temperature = temp_predictor(prev_temps, predict_date)
print(f"The predicted temperature for {predict_date.month}/{predict_date.day} is {predicted_temperature:.1f}°F")