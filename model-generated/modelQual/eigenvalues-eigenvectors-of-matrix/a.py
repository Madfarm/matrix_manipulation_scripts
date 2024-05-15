import numpy as np
from fractions import Fraction

def calculate_eigen(matrix):
    # Ensure the input is a square matrix
    assert len(matrix) == len(matrix[0]), "Input matrix must be square"

    # Compute eigenvalues and eigenvectors using NumPy's built-in function
    eigenvalues, eigenvectors = np.linalg.eig(matrix)

    # Convert eigenvectors to Fractions
    eigenvectors = np.array([np.vectorize(Fraction)(v) for v in eigenvectors.T])

    # Round the eigenvalues to simplify the fractions
    eigenvalues = np.array([Fraction(e).limit_denominator() for e in eigenvalues])

    return eigenvalues, eigenvectors

# Test the function
matrix = [[1,2,3], [4,5,6], [7,8,9]]
eigenvalues, eigenvectors = calculate_eigen(matrix)

print(eigenvalues)
print(eigenvectors)

# Assertions to validate the output
assert len(eigenvalues) == len(matrix), "Number of eigenvalues does not match the size of the matrix"
assert len(eigenvectors) == len(matrix), "Number of eigenvectors does not match the size of the matrix"