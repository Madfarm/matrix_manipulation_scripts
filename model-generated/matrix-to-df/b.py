import pandas as pd


def reverse_rows(matrix):
    # Convert the matrix to a DataFrame
    df = pd.DataFrame(matrix)


    # Reverse the rows of the DataFrame
    df = df.iloc[::-1]


    # Convert the DataFrame back to a matrix
    matrix = df.values.tolist()


    return matrix


# Test the function
matrix = [[10,11,12],
          [13,14,15],
          [16,17,18]]


print("Original matrix:")
for row in matrix:
    print(row)


print("\nReversed matrix:")
for row in reverse_rows(matrix):
    print(row)