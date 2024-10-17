word = input("Enter word: ")
char = input("Enter char: ")
occurrences = []

# Loop through each character in the word
for i in range(len(word)):
    if word[i] == char:
        occurrences.append(i)

# Check if any occurrences were found
if occurrences:
    for i in occurrences:
        print(i)
else:
    print("-1")
