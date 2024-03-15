import math

def squaricles(x):
    if x == 1: return 1
    
    approx = x / 2.0
    while approx * approx - x > 0.5:
        approx = (approx + (x / approx)) / 2.0

    return math.floor(approx)

print(squaricles(17))