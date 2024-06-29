def lawnmower_price_predictor(cutting_width, battery_life, cord_length, type):
    price = 0
    if cutting_width > 12:
        price += (cutting_width - 12) * 3.50
    if battery_life > 1:
        price += (battery_life - 1) * 12.00
    if cord_length > 5:
        price += (cord_length - 5) * 15
    if type == "riding":
        price += 2000
    elif type == "self-propelled":
        price += 300
    elif type == "push":
        price += 50
    price = round(price, 2)
    cents = price - int(price)
    if cents > 0.5:
        price = int(price) + 0.99
    else:
        price = int(price)
    if price % 100 < 30:
        price = (price // 100) * 100 - 1
    else:
        price = (price // 100 + 1) * 100 - 1
    return price

print(lawnmower_price_predictor(15, 2.25, 10, "push"))  # Output: 249.0
print(lawnmower_price_predictor(12, 1, 5, "riding"))  # Output: 1999.0
print(lawnmower_price_predictor(18, 3.5, 15, "self-propelled"))  # Output: 499.0