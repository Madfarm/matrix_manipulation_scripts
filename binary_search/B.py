def binary_search(arr, x):
    """
    Perform binary search to find x in arr.
    
    Args:
    - arr: List of numbers (should be sorted).
    - x: Number to search for.
    
    Returns:
    - Index of x in arr, or -1 if x is not present.
    """
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        # Check if x is present at mid
        if arr[mid] == x:
            return mid
        
        # If x is greater, move to the right side
        elif arr[mid] < x:
            low = mid + 1
        
        # Otherwise, move to the left side
        else:
            high = mid - 1
            
    return -1

# Test case
arr = [1, 2, 68, 100000,]
x = 68
result = binary_search(arr, x)
if result != -1:
    print(f"Element {x} is present at index {result}")
else:
    print(f"Element {x} is not present in the array")