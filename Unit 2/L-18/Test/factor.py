'''This program takes a number as input from the user and finds all of its factors. 
If the number has factors, they are printed. If no factors are found (which is not possible in this case since every 
number has at least 1 as a factor), 
it would print -1.'''
number = int(input("Enter number: "))  # Take an integer input from the user

factor = []  # Initialize an empty list to store factors

# Loop through numbers from 1 to the input number
for i in range(1, number + 1):
    if number % i == 0:  # Check if 'i' is a factor of 'number'
        factor.append(i)  # If yes, add 'i' to the factor list

# If factors are found, print them
if factor:
    for i in factor:
        print(i, end=" ")  # Print each factor followed by a space
else:
    print("-1")  # If no factors are found (which won't happen), print -1
