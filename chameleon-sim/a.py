def average_color(colors):
    """
    Calculate the average color from a list of colors.

    Args:
        colors (list): A list of colors, each represented by a tuple of RGB values.

    Returns:
        tuple: The average color as an RGB tuple.
    """
    # Initialize the sum of RGB values
    total_r, total_g, total_b = 0, 0, 0

    # Calculate the sum of RGB values
    for r, g, b in colors:
        total_r += r
        total_g += g
        total_b += b

    # Calculate the average RGB values
    avg_r = total_r / len(colors)
    avg_g = total_g / len(colors)
    avg_b = total_b / len(colors)

    return (avg_r, avg_g, avg_b)


# Test the function with some example colors
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # Example list of colors (red, green, blue)
avg_color = average_color(colors)
print("Average color:", avg_color)