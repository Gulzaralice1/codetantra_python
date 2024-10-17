# Prompt the user to enter a word
word = input("Enter any word: ")

# Prompt the user to enter a character to search for in the word
char_to_find = input("Enter any char to find in the word: ")

# Initialize an empty list to store the indices of the character found
indices = []

# Loop through each character in the word along with its index
for index, character in enumerate(word):
    # Check if the current character matches the character we are looking for
    if character == char_to_find:
        # If it matches, append the index to the indices list
        indices.append(index)

# Check if the indices list has any elements
if indices:
    # If it has elements, print each index where the character was found
    for i in indices:
        print(i)
else:
    # If no matches were found, print -1
    print(-1)
