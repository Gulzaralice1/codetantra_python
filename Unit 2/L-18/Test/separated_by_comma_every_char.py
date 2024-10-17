string = str(input("Enter word and separate by comma: "))  # Take input as a string from the user

char = ""  # Initialize an empty string 'char'

# Method 1st
for i in range(len(string)):  # Loop through the string using its length
    char += string[i] + ","  # Append each character from the string followed by a comma
print(char)  # Output the final result

# Method second
for index, char in enumerate(string):  # Loop through the string using 'enumerate' to get both index and character
    print(char, end=",")  # Print each character followed by a comma without a newline
