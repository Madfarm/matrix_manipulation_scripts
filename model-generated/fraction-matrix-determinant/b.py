import numpy as np
from fractions import Fraction


def calculate_determinant(matrix):
    # Ensure the matrix contains only Fraction elements
    assert all(isinstance(x, Fraction) for x in matrix.flat), "Matrix must contain only Fraction elements"


    # Calculate the determinant of the matrix
    det = np.linalg.det(matrix.astype(float))


    # Convert the determinant to a Fraction
    det_fraction = Fraction(det).limit_denominator()


    # Convert the original matrix to floats
    matrix_floats = matrix.astype(float)


    # Return a dictionary with the results
    return {'determinant': det_fraction, 'matrix_floats': matrix_floats}


# Test the function
matrix = np.array([[Fraction(1, 2), Fraction(1, 3), Fraction(1, 4)],
                   [Fraction(1, 5), Fraction(1, 6), Fraction(1, 7)],
                   [Fraction(1, 8), Fraction(1, 9), Fraction(1, 10)]])
result = calculate_determinant(matrix)


# Verify the output
assert isinstance(result, dict), "Output must be a dictionary"
assert 'determinant' in result and 'matrix_floats' in result, "Dictionary must contain 'determinant' and 'matrix_floats' keys"
assert isinstance(result['determinant'], Fraction), "Determinant must be a Fraction"
assert result['matrix_floats'].dtype == float, "Matrix must be converted to floats"


print(result)