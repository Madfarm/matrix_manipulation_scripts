import math

def find_root(x, precision=0.00001):
    guess = x / 2.0
    while abs(guess * guess - x) > precision:
        guess = (guess + (x / guess)) / 2.0
    return math.floor(guess)

print(find_root(8))