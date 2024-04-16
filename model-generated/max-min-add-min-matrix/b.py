def transform_matrix(matrix):
    # Find the minimum and maximum values in the matrix
    min_val = min(min(row) for row in matrix)
    max_val = max(max(row) for row in matrix)


    # Replace the maximum value with the minimum value
    for row in matrix:
        for i, val in enumerate(row):
            if val == max_val:
                row[i] = min_val


    # Add the minimum value to each value in the matrix
    for row in matrix:
        for i, val in enumerate(row):
            row[i] += min_val


    return matrix


# Test the function
matrix = [[3, 5, 8, 10],
          [6, 7, 12, 14],
          [4, 15, 9, 20],
          [18, 21, 24, 28]]


assert transform_matrix(matrix) == [[6, 8, 11, 13],
                                    [9, 10, 15, 17],
                                    [7, 18, 12, 23],
                                    [21, 24, 27, 31]]