import timeit

def iterative_binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # not found

def recursive_binary_search(arr, target):
    def inner(low, high):
        if high < low:
            return -1  # not found
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return inner(mid + 1, high)
        else:
            return inner(low, mid - 1)
    return inner(0, len(arr) - 1)

# Set up the test data
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5

# Time the iterative implementation
print("Iterative implementation:")
t = timeit.timeit(lambda: iterative_binary_search(arr, target), number=10000)
print(f"Time: {t:.4f} seconds")

# Time the recursive implementation
print("Recursive implementation:")
t = timeit.timeit(lambda: recursive_binary_search(arr, target), number=10000)
print(f"Time: {t:.4f} seconds")