# Print square of all even number 
# Number  [1,2,3,4,5,6,7,8,9]

Number = [1,2,3,4,5,6,7,8,9]

# Make a function for even square only
def even_square(number):
    if number % 2 == 0:
        return number**2
    else:
        return number

# Now make a map function 
mapped_object = map(even_square,Number)
print(list(mapped_object))