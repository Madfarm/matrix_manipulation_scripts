def powerset(arr):
    """
    Returns every possible subset from a given array
    """
    def backtrack(arr, subset, index):
        if index == len(arr):
            # Reached the end of the array, add the current subset to the result
            result.append(subset[:])
        else:
            # Try including the current element in the subset
            subset.append(arr[index])
            backtrack(arr, subset, index + 1)
            # Try excluding the current element from the subset
            subset.pop()
            backtrack(arr, subset, index + 1)

    result = []
    backtrack(arr, [], 0)
    return result

arr = [1, 2, 3, 4]
print(powerset(arr)) 