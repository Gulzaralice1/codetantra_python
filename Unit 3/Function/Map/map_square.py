# print square of all number using MAP function 
# Number are [1,2,3,4,5,6]
# square are [1, 4, 9, 16, 25, 36]
Number = [1,2,3,4,5,6]

#Make a function and pass number for square 
def square(number):
    return number**2

# Make variable and map function
mapped_obj = map(square,Number)  # square its function number is  [1,2,3,4,5,6]

# Here print square 
print(list(mapped_obj))
