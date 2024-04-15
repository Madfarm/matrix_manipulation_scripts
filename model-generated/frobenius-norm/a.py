def frobenius_norm(arr):
    # Validate the input array
    assert isinstance(arr, list), "Input must be a list"
    for row in arr:
        assert isinstance(row, list), "Each element of the input list must be a list"
        for elem in row:
            assert isinstance(elem, (int, float)), "Each element of the sublists must be a number"


    # Calculate the Frobenius norm
    norm = 0
    for row in arr:
        for elem in row:
            norm += abs(elem) ** 2
    norm = norm ** 0.5


    return norm


# Test the function with the provided input
arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
assert frobenius_norm(arr) == 25.495097567963924, "The calculated Frobenius norm is incorrect"