# the Type of Triangle Based on Side Lengths
a = int(input("Enter side 1st: "))  # Take input for the first side of the triangle
b = int(input("Enter side 2nd: "))  # Take input for the second side of the triangle
c = int(input("Enter side 3rd: "))  # Take input for the third side of the triangle

# Check if all sides are equal
if a == b == c:
    print("Equilateral triangle")  # An equilateral triangle has all three sides equal

# Check if any two sides are equal
elif a == b or a == c or b == c:
    print("Isosceles triangle")  # An isosceles triangle has two sides equal

# If no sides are equal, it's a scalene triangle
else:
    print("Scalene triangle")  # A scalene triangle has all sides of different lengths
