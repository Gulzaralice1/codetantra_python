# Basic Level Questions
# String Split
# Write a program that takes a comma-separated string of names from the user and converts it into a list of names. Print the list.
string = str(input("Enter names i will separatedea with comma: "))


# using split() for convet into list and with comma
words = string.split()
print(words)

# Here using join() function and remve comma print space
print(" ".join(words))

# print with  space
print(" ".join(words))



# output
# ['gulzar', 'alice', 'lpu']
# gulzar alice lpu
# gulzar alice lpu