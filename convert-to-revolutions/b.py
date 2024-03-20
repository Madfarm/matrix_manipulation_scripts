def convert_to_revolutions(angle):
    revolutions = abs(angle) // 360
    remaining_angle = angle - (revolutions * 360)
    return remaining_angle, revolutions

# Testing the function
angle = 750
remaining_angle, revolutions = convert_to_revolutions(angle)
print("The angle {}° takes {} revolutions and {}° remain".format(angle, revolutions, remaining_angle))