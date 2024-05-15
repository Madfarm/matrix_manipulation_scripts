import numpy as np
from fractions import Fraction

def calculate_eigen(matrix):
    # Ensure the input is a square matrix
    assert len(matrix) == len(matrix[0]), "Input matrix must be square"
    
    # Convert the input matrix to a numpy array with Fraction type
    matrix = np.array(matrix, dtype=object)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            matrix[i, j] = Fraction(matrix[i, j]).limit_denominator()
    
    # Calculate the eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    
    # Convert the eigenvalues to Fraction type
    eigenvalues = [Fraction(e).limit_denominator() for e in eigenvalues]
    
    return eigenvalues, eigenvectors

# Test the function
matrix = [[1,2,3], [4,5,6], [7,8,9]]
eigenvalues, eigenvectors = calculate_eigen(matrix)

# Print the results
print("Eigenvalues:")
for eigenvalue in eigenvalues:
    print(eigenvalue)
print("\nEigenvectors:")
for eigenvector in eigenvectors:
    print(eigenvector)

# Assertions to validate the output
assert len(eigenvalues) == len(matrix), "Number of eigenvalues does not match the size of the input matrix"
assert len(eigenvectors) == len(matrix), "Number of eigenvectors does not match the size of the input matrix"