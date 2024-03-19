def min_max_sum(arr):
    arr.sort()
    min_sum = sum(arr[:-1])
    max_sum = sum(arr[1:])
    print(min_sum, max_sum)

# Test the function
min_max_sum([1, 3, 5, 7, 9])