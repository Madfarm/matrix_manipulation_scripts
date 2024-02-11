def powerset(arr):
    """
    Returns every possible subset from a given array
    """
    subsets = []
    for i in range(2**len(arr)):
        subset = []
        for j in range(len(arr)):
            if (i >> j) & 1:
                subset.append(arr[j])
        subsets.append(subset)
    return subsets

arr = [1, 2, 3, 4]
print(powerset(arr))