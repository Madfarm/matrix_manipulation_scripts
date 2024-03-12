def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

day = 10  # change this value to calculate the number of roses on a different day
roses = fibonacci(day)
print(f"On day {day}, the rosebush will be blooming {roses} roses.")