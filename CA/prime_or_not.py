import math

num = int(input("Enter a number to check if it's prime: "))

# Edge case handling
if num <= 1:
    print("This number is less than or equal to 1 and thus not a prime number.")
elif num == 2:
    print(f"{num} is the smallest prime number.")
else:
    is_prime = True  # Assume the number is prime
    # Check for factors from 2 to sqrt(num)
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
