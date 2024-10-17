# This program takes an integer as input and prints each digit of the number on a new line. 
# It demonstrates two different methods to achieve this.
number = int(input("Enter number: "))  # Take an integer input from the user

# Method 1
string = str(number)  # Convert the number to a string
for i in range(len(string)):  # Loop through each character using its length
    print(string[i])  # Print each character (digit) on a new line

# Method 2
for i in str(number):  # Directly loop through the string version of the number
    print(i)  # Print each character (digit) on a new line
