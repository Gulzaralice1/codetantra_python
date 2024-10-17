# Replace Word

# Write a function that takes a string and two words (old and new) as input, 
# and replaces all occurrences of the old word with the new word. Print the modified string.

string = str(input("Enter string :"))
old = str(input("Enter old : "))
new = str(input("Enter new : "))
replace_string = string.replace(old,new)
print(replace_string)


# Enter string :hello python devloper
# Enter old : python
# Enter new : c++
# hello c++ devloper