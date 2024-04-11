import numpy as np

def find_diagonal(a, b):
    # Compute the dot product
    result = a.dot(b)
    
    # Extract and return the diagonal elements
    return np.diag(result)

# Input arrays
a = np.array([[1, 2], [3, 4]])
b = np.array([[1, 0], [0, 1]])

# Expected output for verification
expected_output = np.array([1, 4])

# Calculate the actual output
actual_output = find_diagonal(a, b)

assert (np.allclose(actual_output, expected_output)), f"Expected {expected_output}, but got {actual_output}"