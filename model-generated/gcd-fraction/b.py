import math


def reduce_fraction(numerator, denominator):
    gcd = math.gcd(numerator, denominator)
    return numerator // gcd, denominator // gcd


def power_fraction(fraction, exponent):
    numerator, denominator = fraction
    assert denominator != 0, "Denominator cannot be zero"


    new_numerator = numerator ** exponent
    new_denominator = denominator ** exponent


    reduced_numerator, reduced_denominator = reduce_fraction(new_numerator, new_denominator)


    assert reduced_denominator > 0, "Denominator must be positive"


    return reduced_numerator, reduced_denominator


fraction = (3, 4)
exponent = 2
assert power_fraction(fraction, exponent) == (9, 16)