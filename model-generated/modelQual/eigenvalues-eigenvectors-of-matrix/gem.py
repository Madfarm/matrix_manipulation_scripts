import numpy as np
from fractions import Fraction

def calculate_eigen(matrix):
    """
    Calculate the eigenvalues and eigenvectors of a square matrix.

    Args:
    matrix (np.ndarray): Square matrix represented as a 2D NumPy array.

    Returns:
    (np.ndarray, np.ndarray): Tuple containing eigenvalues and eigenvectors.
    
    Raises:
    ValueError: If the input matrix is not square.
    """
    # Check if the matrix is square
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Input matrix is not square")

    # Convert elements of the matrix to Fractions
    # matrix_fractions = np.vectorize(Fraction)(matrix)

    # Compute eigenvalues and eigenvectors using NumPy's built-in function
    eigenvalues, eigenvectors = np.linalg.eig(matrix)

    # Convert eigenvectors to Fractions
    eigenvectors = np.array([np.vectorize(Fraction)(v) for v in eigenvectors.T])

    # Round the eigenvalues to simplify the fractions
    eigenvalues = np.array([Fraction(e).limit_denominator() for e in eigenvalues])

    return eigenvalues, eigenvectors

# Test the program with the given matrix
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

eigenvalues, eigenvectors = calculate_eigen(matrix)

print("Eigenvalues:")
print(eigenvalues)
print("\nEigenvectors:")
print(eigenvectors)