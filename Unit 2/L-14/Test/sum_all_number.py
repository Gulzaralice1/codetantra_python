# Take a two-digit positive integer and find the sum of the digits of that number. print the number itself if
# the sum is below 10, otherwise print "invalid".

two_digit = int(input("Enter positive two digit number: "))
once = two_digit % 10
tense = two_digit // 10
add =  once + tense

if add >= 10:
    print(two_digit)
else:
    print("invalid")

