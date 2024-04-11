import numpy as np

def sort_by_column(arr, n):
  """
  Sorts a NumPy array by the nth column.

  Args:
    arr: The NumPy array to sort.
    n: The index of the column to sort by (0-based indexing).

  Returns:
    A new NumPy array sorted by the nth column.
  """

  return arr[arr[:, n].argsort()]

# Example usage
arr = np.array([[3, 1, 4], [2, 2, 2], [1, 3, 1]])
sorted_arr = sort_by_column(arr.copy(), 1)  # Sort by the second column (n=1)

print(sorted_arr)