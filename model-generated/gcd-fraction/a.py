import math


def raise_fraction_to_power(fraction, exponent):
    numerator, denominator = fraction
    assert denominator != 0, "Denominator cannot be zero"


    # Calculate the result of raising the fraction to the power
    result_numerator = numerator ** exponent
    result_denominator = denominator ** exponent


    # Reduce the resulting fraction
    gcd = math.gcd(result_numerator, result_denominator)
    reduced_numerator = result_numerator // gcd
    reduced_denominator = result_denominator // gcd


    return reduced_numerator, reduced_denominator


# Test the function
fraction = (3, 4)
exponent = 2
result = raise_fraction_to_power(fraction, exponent)
print(result)


# Verify the calculations and output
assert result == (9, 16), f"Expected (9, 16) but got {result}"