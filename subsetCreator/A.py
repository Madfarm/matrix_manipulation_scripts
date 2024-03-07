def get_subsets(array):
    n = len(array)
    output = []

    # for each mask from 0 to 2**n-1
    for bit in range(2**n):
        # create binary representation of mask
        bin_mask = bin(bit)[2:].zfill(n)
        # use binary mask to generate a subset
        output.append([array[i] for i in range(n) if bin_mask[i]=='1'])
    return output

array = [1, 2, 3]
print(get_subsets(array))