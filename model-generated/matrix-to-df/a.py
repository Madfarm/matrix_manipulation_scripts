import pandas as pd


def reverse_rows(matrix):
    # Convert the matrix to a DataFrame
    df = pd.DataFrame(matrix)

    print("Origiu")
    print(df)

    # Reverse the rows
    df = df.iloc[::-1]


    return df


# Test the function
matrix = [[10,11,12],
          [13,14,15],
          [16,17,18]]


print(reverse_rows(matrix))