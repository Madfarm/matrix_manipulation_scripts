def convert_to_revolutions(angle):
    revolutions = angle // 360
    remaining_angle = angle % 360
    return remaining_angle, revolutions

# Test the function
angle = 750
remaining_angle, revolutions = convert_to_revolutions(angle)
print(f"For an angle of {angle}°, it takes {revolutions} revolutions. The remaining angle is {remaining_angle}°.")