# def apply_operations(int, filter):
#     for op in filter:
#         int = eval(str(int) + op)
#     return int

# # Testing the function
# filter = ["* 0.9", "+ 2", "* 0.7", "- 1", "/ 0.5"]
# print(apply_operations(10, filter))


def apply_operations(int, filter):
    for operation in filter:
        int = eval(str(int) + operation)
    return int

print(apply_operations(10, ["* 0.9", "+ 2", "* 3", "- 4", "/ 2"]))