def binary_search_iterative(arr, x):
    """Performs binary search (iterative implementation)"""
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == x:
            return mid  # Found at this index

        elif arr[mid] < x:
            low = mid + 1  # Search in right half

        else:
            high = mid - 1  # Search in left half

    return -1  # Not found


# Test Case
arr = [2, 3, 4, 10, 11, 21, 40]
x = 11

result = binary_search_iterative(arr, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")