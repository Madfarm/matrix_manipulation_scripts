def sort_fractions(fractions):
    assert isinstance(fractions, list), "Input must be a list of tuples"
    for fraction in fractions:
        assert isinstance(fraction, tuple) and len(fraction) == 2, "Each fraction must be a tuple with two elements"
        assert all(isinstance(i, int) for i in fraction), "Numerator and denominator must be integers"
        assert fraction[1] != 0, "Denominator cannot be zero"


    sorted_fractions = sorted(fractions, key=lambda x: x[0]/x[1])
    return sorted_fractions


fractions = [(3, 5), (1, 2), (2, 3), (4, 7)]
assert sort_fractions(fractions) == [(1, 2), (4, 7), (3, 5), (2, 3)]