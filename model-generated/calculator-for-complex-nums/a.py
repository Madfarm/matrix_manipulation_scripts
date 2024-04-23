import cmath


def complex_operation(z1, z2, operation):
    if operation == 'addition':
        return z1 + z2
    elif operation == 'subtraction':
        return z1 - z2
    elif operation == 'multiplication':
        return z1 * z2
    elif operation == 'division':
        return z1 / z2
    else:
        raise ValueError("Invalid operation. Please choose from: addition, subtraction, multiplication, division")


# Test the function
z1 = complex(3, 2)
z2 = complex(1, 7)


operations = ['addition', 'subtraction', 'multiplication', 'division']


for operation in operations:
    result = complex_operation(z1, z2, operation)
    print(f"Complex {operation}: {result}")