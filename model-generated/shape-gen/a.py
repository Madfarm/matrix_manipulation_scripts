import pandas as pd
import numpy as np


def generate_shapes(num_shapes, min_radius, max_radius, min_side_length, max_side_length):
    assert num_shapes > 0, "Number of shapes must be greater than 0"
    assert min_radius > 0 and max_radius > 0, "Radius must be greater than 0"
    assert min_side_length > 0 and max_side_length > 0, "Side length must be greater than 0"
    assert min_radius < max_radius, "Minimum radius must be less than maximum radius"
    assert min_side_length < max_side_length, "Minimum side length must be less than maximum side length"


    shape_types = ['circle', 'square', 'triangle']
    shapes = []


    for _ in range(num_shapes):
        shape_type = np.random.choice(shape_types)


        if shape_type == 'circle':
            radius = np.random.uniform(min_radius, max_radius)
            area = np.pi * (radius ** 2)
            shapes.append({'Shape Type': shape_type, 'Radius': radius, 'Area': area})


        elif shape_type == 'square':
            side_length = np.random.uniform(min_side_length, max_side_length)
            area = side_length ** 2
            shapes.append({'Shape Type': shape_type, 'Side Length': side_length, 'Area': area})


        elif shape_type == 'triangle':
            while True:
                sides = np.random.uniform(min_side_length, max_side_length, 3)
                sides.sort()
                if sides[0] + sides[1] > sides[2]:
                    break
            # Heron's formula to calculate the area of a triangle
            semi_perimeter = sum(sides) / 2
            area = np.sqrt(semi_perimeter * (semi_perimeter - sides[0]) * (semi_perimeter - sides[1]) * (semi_perimeter - sides[2]))
            shapes.append({'Shape Type': shape_type, 'Side Length': sides, 'Area': area})


    df = pd.DataFrame(shapes)
    assert not df.empty, "DataFrame is empty"
    return df


# Demonstration
num_shapes = 10
min_radius = 2
max_radius = 5
min_side_length = 3
max_side_length = 8


df = generate_shapes(num_shapes, min_radius, max_radius, min_side_length, max_side_length)
print(df)