savings = 0
for i in range(1, 481):
    savings = savings + 200000
    savings = savings * 1.07

    if (i % 12 == 0):
        savings = savings * 0.87

print(f"You would have {savings/1000000000} billion")