# # program to hcf and gcd of two numbers
# 56 98
# 14
a = int(input("Enter number 1st: "))
b = int(input("Enter number 2st: "))

while b != 0:
    a , b = b, (a%b)

print(a)