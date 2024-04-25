from fractions import Fraction


def add_fractions(fractions):
    # Validate input
    assert len(fractions) == 2, "Input must be a list of two fractions"
    for fraction in fractions:
        assert isinstance(fraction, tuple), "Each fraction must be a tuple"
        assert len(fraction) == 2, "Each fraction must have two elements"
        assert all(isinstance(part, int) for part in fraction), "Numerator and denominator must be integers"
        assert fraction[1] != 0, "Denominator cannot be zero"


    # Convert tuples to Fractions and add them
    result = sum(Fraction(*fraction) for fraction in fractions)


    # Validate output
    assert isinstance(result, Fraction), "Result must be a Fraction"


    return result


# Test the function
fraction1 = (3, 5)
fraction2 = (2, 7)
assert add_fractions([fraction1, fraction2]) == Fraction(31, 35)