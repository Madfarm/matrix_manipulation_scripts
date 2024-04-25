from fractions import Fraction


def add_fractions(fractions):
    # Check if input is a list of two tuples
    assert isinstance(fractions, list) and len(fractions) == 2, "Input must be a list of two tuples"


    # Check if each tuple contains two integers
    for fraction in fractions:
        assert isinstance(fraction, tuple) and len(fraction) == 2, "Each fraction must be a tuple of two integers"
        assert all(isinstance(i, int) for i in fraction), "Each fraction must be a tuple of two integers"
        assert fraction[1] != 0, "Denominator cannot be zero"


    # Convert tuples to Fractions and add them together
    result = sum(Fraction(*fraction) for fraction in fractions)


    # Check if result is an instance of Fraction
    assert isinstance(result, Fraction), "Result must be a Fraction"


    return result


# Test the function
fraction1 = (3, 5)
fraction2 = (2, 7)
print(add_fractions([fraction1, fraction2]))