def powerset(arr):
    """
    Returns every possible subset from the given array.
    """
    n = len(arr)
    subsets = []
    for i in range(2**n):
        subset = []
        for j in range(n):
            if (i & (1 << j)) != 0:
                subset.append(arr[j])
        subsets.append(subset)
    return subsets

arr = [1, 2, 3,4]
print(powerset(arr))