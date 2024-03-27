def validate_fermat_theorem(species):
    # Iterate over each species
    for a in species:
        # Iterate over each species excluding the current species
        for b in species:
            if a != b:
                # Calculate c as the difference between the sum of squares of a and b and the square of the product of a and b
                c = (a2 + b2) - (a*b)2
                # Check if c is a perfect square and is greater than 2
                if c0.5 == int(c**0.5) and c > 2:
                    # If c is a perfect square and greater than 2, print the ages and return False
                    print(f"Species with ages {a}, {b}, and {c} violate the theorem.")
                    return False
    # If no violation is found, print a success message and return True
    print("No combination of ages violates the theorem.")
    return True