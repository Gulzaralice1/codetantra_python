# Accessing Characters: You can access characters in a string using indexing
string = "python"
print("Original String:", string)
print("Character at index 0:", string[0])  # Output: p
print("Character at index 1:", string[1])  # Output: y
print("Character at index 2:", string[2])  # Output: t
print("Character at index -1 (last):", string[-1])  # Output: n
print("Character at index -2:", string[-2])  # Output: o
print("Character at index -3:", string[-3])  # Output: h

# Slicing: Extract a part of a string using the slicing operator [:]
print("\nSlicing Examples:")
print("All characters:", string[:])  # Outputs entire string
print("From index 0 to the end:", string[0:])  # Outputs: python
print("From index 0 to 5:", string[:5])  # Outputs: pytho
print("From index 3 to the end:", string[3:])  # Outputs: hon
print("From index -1 to the end:", string[-1:])  # Outputs: n
print("From start to index -1:", string[:-1])  # Outputs: pytho

# Reverse a String Using Slicing
print("\nReversed String:")
print(string[::-1])  # Outputs: nohtyp

# String Operations
print("\nString Operations:")
print("Concatenation Example:")
string1 = "Hello"
string2 = "World"
print("Concatenated:", string1 + " " + string2)  # Outputs: Hello World

print("\nRepetition Example:")
print("Repeating 'python' 3 times:", string * 3)  # Outputs: pythonpythonpython

print("\nLength of the String:")
print("Length of 'python':", len(string))  # Outputs: 6

# String Methods
string3 = "hello world"
string4 = "HeeLO"
print("\nString Methods:")
print("UPPER:", string.upper())
print("LOWER:", string.lower())
print("TITLE:", string3.title())
print("CAPITALIZE:", string.capitalize())
print("SWAPCASE:", string4.swapcase())  # Changes each char upper to lower, lower to upper

# Stripping Whitespace
# Stripping Whitespace Examples
print("\nStripping Whitespace Examples:")
print("Original with spaces:", '   python   ')
print("strip() - Removes all spaces:", '   python   '.strip())
print("rstrip() - Removes right spaces:", '   python   '.rstrip())
print("lstrip() - Removes left spaces:", '   python   '.lstrip())


# Searching & Replacing
text = "hello, world my name is gulzar"
print("\nSearching & Replacing")
print("find(), index(), replace()")

# Finding substrings
print("Find 'world':", text.find("world"))  # Returns the index of the first occurrence of 'world'
print("Find 'gulzar':", text.find("gulzar"))  # Returns the index of the first occurrence of 'gulzar'
print("Find 'notfound':", text.find("notfound"))  # Returns -1 if not found

# Indexing substrings (will raise an error if not found)
print("\nIndex 'world':", text.index("world"))  # Returns the index of the first occurrence of 'world'
print("Index 'gulzar':", text.index("gulzar"))  # Returns the index of the first occurrence of 'gulzar')
# Uncommenting the next line will raise a ValueError as 'notfound' is not in the string
# print("Index 'notfound':", text.index("notfound")) 

# Replacing substrings
replaced_text = text.replace("gulzar", "John")
print("\nReplacing 'gulzar' with 'John':", replaced_text)



# Splitting & Joining
print("Splitting & Joining")

# Splitting a string into a list of words
text = "hello world"
words = text.split(" ")  # Split by space
print("Split words:", words)

# Joining the words back into a string with different delimiters
print("Join with space:", " ".join(words))  # Joining with a space
print("Join with comma:", ",".join(words))  # Joining with a comma

# Splitting a string without specifying a separator
text = "apple banana cherry"
print("Split fruits:", text.split())  # Split by whitespace (default)

# Splitting a string with a specific separator
number = "1,2,3,4,5"
print("Split numbers:", number.split(","))  # Split by comma


text = "Hello"

# You cannot directly modify a string like this
# text[0] = "h"  # This will generate an error

# Instead, you can create a new string
new_text = "gulzar" + text[:]  # Concatenating 'gulzar' with the entire original string 'Hello'
print("New text:", new_text)

# Inserting an underscore after the 6th character
new_text2 = new_text[0:6] + "_" + new_text[6:]  # Insert '_' after 'gulzar'
print("New text with underscore:", new_text2)

