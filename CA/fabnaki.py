# Number of terms
n = 10

# Initial two terms of the Fibonacci sequence
a, b = 0, 1

# Print the first two terms
print("F(0) =", a)
print("F(1) =", b)

# Generate and print the rest of the sequence
for i in range(2, n):
    a, b = b, a + b
    print( b)
