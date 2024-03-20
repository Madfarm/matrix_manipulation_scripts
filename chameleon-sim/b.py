def average_color(colors):
    # Initialize the total red, green, and blue values
    total_r = 0
    total_g = 0
    total_b = 0
    
    # Calculate the total red, green, and blue values
    for color in colors:
        total_r += color[0]
        total_g += color[1]
        total_b += color[2]
    
    # Calculate the average red, green, and blue values
    avg_r = total_r / len(colors)
    avg_g = total_g / len(colors)
    avg_b = total_b / len(colors)
    
    # Return the average color as an RGB tuple
    return (avg_r, avg_g, avg_b)

# Test the function
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # Example list of colors
average = average_color(colors)
print("The average color is:", average)