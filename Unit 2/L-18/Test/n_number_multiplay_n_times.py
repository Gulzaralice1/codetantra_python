# This program takes a number as input from the user and multiplies it by itself repeatedly (n-1) times. 
# Essentially, this computes the power of the number raised to (n-1)
number = int(input("Enter number: "))  # Take an integer input from the user
multiplay = 1  # Initialize 'multiplay' to 1

# Loop from 1 to (number - 1) to multiply the number by itself
for i in range(1, number):
    multiplay *= number  # Multiply 'multiplay' by the input number in each iteration

print(multiplay)  # Output the final result after the loop
