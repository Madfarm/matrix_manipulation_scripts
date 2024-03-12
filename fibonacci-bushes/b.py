def fibonacci(n):
    if n <= 0:
        return "Invalid day"
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

day = 10  # replace 10 with the day you want to calculate
print("Number of roses on day", day, ":", fibonacci(day))