# Ask the user to enter a number to check if it's a perfect number
number_to_check = int(input("Enter a number to check if it's perfect or not: "))

# List to store the factors of the number
factors = []

# Variable to store the sum of the factors
sum_of_factors = 0

# Loop through numbers from 1 to (number_to_check - 1) to find factors
for i in range(1, number_to_check):
    # Check if 'i' is a factor of 'number_to_check'
    if number_to_check % i == 0:
        factors.append(i)         # Add the factor to the list
        sum_of_factors += i      # Add the factor to the sum

# Check if the sum of the factors equals the original number
if sum_of_factors == number_to_check:
    print(number_to_check, "is a perfect number.")
else:
    print(number_to_check, "is not a perfect number.")

# Print the list of factors
print("These are the factors: ", factors)
