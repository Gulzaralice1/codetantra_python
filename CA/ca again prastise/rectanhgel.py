def can_form_rectangle(sides):
    # Sort the sides
    sides.sort()
    print(sides)
    # Check if the first two sides are equal and the last two sides are equal
    if sides[0] == sides[1] and sides[2] == sides[3]:
        return "possible"
    else:
        return "not possible"

# Example usage
sides = [4, 2, 2, 4]
print(can_form_rectangle(sides))  # Output: possible

sides = [1, 2, 3, 4]
print(can_form_rectangle(sides))  # Output: not possible
