# Take a string of fixed length 6, if the first two characters of a given string are similar to the last two
# characters (Order doesn't matter) then print the string with only the first two and last two
# characters excluding the remaining characters or else it should print the remaining characters
# excluding the first two and last two characters.

# first two char and lasgt two char are same not if same then print yes else  print middle two total char 6

char = str(input("Enter  6 letter char : "))
first2Letter = char[:2]
lastt2Letter = char[-2:]

if (set(first2Letter) == set(lastt2Letter)):
    print(first2Letter+lastt2Letter)
else:
    print(char[2:4])



# OUTPUT
#1.  Enter  6 letter char : python
# th


#2.  Enter  6 letter char : pyuiyp
# pyyp