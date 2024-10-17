# Accessing Characters: You can access characters in a string using indexing
string = "python"
print(string)
print("p access char with index 0",string[0]) #p
print("y access char with index 1",string[1]) #y
print("t access char with index 2",string[2]) #t
print("n access char with index -1",string[-1]) #n
print("o access char with index -2",string[-2]) #o
print("h access char with index -3",string[-3]) #h


print("\n\n")
# Slicing: Extract a part of a string using the slicing operator [:]
print("Slicing: Extract a part of a string using the slicing operator")
print(string)
print("All char:- ",string[:])  #print all char
print("from index 0 to the end:- ",string[0:]) # print from 0 to all
print("from index 0 to the 5:- ",string[:5]) #0 to o
print("from index 3 to the end:- ",string[3:]) # Output: python! (from index 3 to the end)
print("from index -1 to the end:- ",string[-1:])  # Output: python! (from index -1 to the end)
print("from index -1 to the end:- ",string[:-1])  # Output: python! (from index -1 to the end)



print("\n\n")
print("Reverse a String Using Slicing:")
print(string[::-1]) #print reverse 