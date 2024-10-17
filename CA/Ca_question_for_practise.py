
# 1 program to sort the words in alphabetical order
# 2 program to remove duplicate elements
# 3 program to merge two dictionaries
# 4 program to add two matrix
# 5 program to multiply two matrix
# 6 write a program to display the multiplication table
# 7 write a program to check whether a number is prime or not.
# 8 program to hcf and gcd of two numbers
# 9 program to get substring out of a string

n = 200
m = 50
result= [ ]
for i in range(1, n):
    if i % 50 == 0:
        result.append(i)


if result:
    print(list(result))
else:
    print("-1")
