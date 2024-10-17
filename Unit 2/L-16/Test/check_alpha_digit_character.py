# This program takes a string input and checks whether the last character is an alphabet, a digit, or another character.
number = input("Enter number to check digit, character, or alpha: ")  # Take input as a string from the user

last_char = number[-1]  # Get the last character of the input

# Check if the last character is an alphabet
if last_char.isalpha():
    print("alpha")  # If it's an alphabetic character, print "alpha"

# Check if the last character is not a digit
elif not last_char.isdigit():
    print("char")  # If it's not a digit, print "char"

# Otherwise, it must be a digit
else:
    print("digit")  # If it's a digit, print "digit"
