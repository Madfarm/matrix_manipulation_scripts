def complex_arithmetic(z1, z2, operation):
    if operation == 'addition':
        return z1 + z2
    elif operation == 'subtraction':
        return z1 - z2
    elif operation == 'multiplication':
        return z1 * z2
    elif operation == 'division':
        if z2 != 0:
            return z1 / z2
        else:
            raise ValueError("Cannot divide by zero")
    else:
        raise ValueError("Invalid operation")


# Test the function
z1 = complex(3, 2)
z2 = complex(1, 7)


result = complex_arithmetic(z1, z2, 'multiplication')
assert result == complex(-11, 23), f"Expected {complex(-11, 23)} but got {result}"
