# Substring Search

# Write a program that asks the user for a string and a substring. 
# The program should find and print the index of the first occurrence of the substring in the string. 
# If the substring is not found, print a message indicating that.

string = str(input("Enter string: "))
sub_string = str(input("Enter sub string: "))

# find substring using FIND()
print("find() : ",string.find(sub_string))

# find substring using index()
# its generate error if not found substring in string
print("index(): ",string.find(sub_string))


# # Check if the substring was found
index_of_substring = string.find(sub_string)
if  sub_string in string:
    print(f"'{sub_string}' in '{string}' with index no '{index_of_substring}'")
else:
    print(f"{sub_string } not found in {string}")




# Enter string: hello gulzar alice
# Enter sub string: gulzar
# find() :  6
# index():  6
# 'gulzar' in 'hello gulzar alice' with index no '6'