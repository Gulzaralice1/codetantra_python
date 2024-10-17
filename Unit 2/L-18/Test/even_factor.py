# This program asks for a number and finds all its even factors. If no even factors are found, it prints -1.
number = int(input("Enter number: "))  # Take an integer input from the user

even_factor = []  # Initialize an empty list to store even factors

# Loop through the numbers from 1 to the input number
for i in range(1, number+1):
    # Check if 'i' is a factor of 'number' and is even
    if number % i == 0 and i % 2 == 0:
        even_factor.append(i)  # If both conditions are true, add 'i' to even_factor list

# If there are even factors, print them
if even_factor:
    for i in even_factor:
        print(i, end=" ")  # Print each even factor followed by a space
else:
    print("-1")  # If no even factors were found, print -1
