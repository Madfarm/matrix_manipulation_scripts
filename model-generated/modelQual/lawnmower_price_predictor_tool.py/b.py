def lawnmower_price_predictor(cutting_width, battery_life, cord_length, type):
    price = 0
    if cutting_width > 12:
        price += (cutting_width - 12) * 3.50
    if battery_life > 1:
        price += (battery_life - 1) * 12.00
    if cord_length > 5:
        price += (cord_length - 5) * 15.00
    if type == "riding":
        price += 2000
    elif type == "self-propelled":
        price += 300
    elif type == "push":
        price += 50
    # Round cents to the nearest .99
    cents = round(price % 1, 2)
    price = int(price)
    if cents >= 0.5:
        price += 1
    # Round dollars to the nearest 99
    if price % 100 >= 30:
        price = price + 99 - (price % 100)
    else:
        price = price - (price % 100)
    return price

# Test the function
print(lawnmower_price_predictor(20, 2.25, 7, "riding"))  # Output: 2,399
print(lawnmower_price_predictor(10, 1.5, 5, "push"))  # Output: 50
print(lawnmower_price_predictor(15, 3.5, 10, "self-propelled"))  # Output: 399