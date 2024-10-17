# Filter Function
number = [67,89,91,34,55,45,46,78]
def filter_even(val):
    if val % 2 == 0:
        return True
    
filter_object = filter(filter_even, number)
print(list((filter_object)))
print(list((filter_object)))  # this is empty becase we can use at only one times