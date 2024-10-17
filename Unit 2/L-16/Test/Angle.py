# print angle
angle = int(input("Enter angle: "))  # Take an angle input from the user

# Check if the angle is a valid type
if angle == 90:
    print("Right angle triangle")
elif angle > 0 and angle < 90:
    print("Acute angle")
elif angle > 90 and angle < 180:
    print("Obtuse angle")
elif angle == 180:
    print("Straight angle")
else:
    print("Invalid angle")
