# Basic Level Questions
# Count Vowels
# Write a function that takes a string as input and returns the number of vowels in that string.
string = str(input("Enter string i will show vowels: "))
vowel = ""
count = 0
for i in string:
    if i in  "aeiouAEIOU":
        vowel+=i
        count+=1

print(vowel ," ",count)


# output
# Enter string i will show vowels: gulzar
# ua   2