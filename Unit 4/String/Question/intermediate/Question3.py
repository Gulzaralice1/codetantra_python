# Palindrome Check

# Write a program that checks if a given string is a palindrome 
# (reads the same forwards and backwards). Ignore spaces and punctuation.

palindorm = input("enter word for Palindrome: ")

reverse_palindorm = palindorm[::-1]
if palindorm == reverse_palindorm:
    print("yes")
else:
    print("no")