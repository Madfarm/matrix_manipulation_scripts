
def convert_float_to_int(arr):
    for i in range(len(arr)):
        arr[i] = int(arr[i])
    return arr


# Test the function
arr = [1.0, 5.0, 12.0, 4.0, 5.6, 9.0]
print("Original array: ", arr)
print("Converted array: ", convert_float_to_int(arr))