import timeit

def binary_search_iterative(arr, target):
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

def binary_search_recursive(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low > high:
        return -1  # not found
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid+1, high)
    else:
        return binary_search_recursive(arr, target, low, mid-1)

def test_binary_search(arr, target, num_iterations=1000):
    setup = f"arr = {arr}; target = {target}"
    iterative_stmt = "binary_search_iterative(arr, target)"
    recursive_stmt = "binary_search_recursive(arr, target)"

    iterative_time = timeit.timeit(iterative_stmt, setup, number=num_iterations)
    recursive_time = timeit.timeit(recursive_stmt, setup, number=num_iterations)

    print(f"Iterative implementation took {iterative_time:.2f} seconds")
    print(f"Recursive implementation took {recursive_time:.2f} seconds")

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
test_binary_search(arr, target)