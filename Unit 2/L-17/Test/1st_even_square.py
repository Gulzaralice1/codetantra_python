# take a number from user and print sum of square of all even number
# 6:- (2 + 4 + 6)--> even number now square and summ 
num = int(input("Enter number for even square: "))
i = 1
squareOfEvenNumber = 0
while i <= num :
    if i % 2 == 0:
        squareOfEvenNumber+= i**2
        print(i**2)
    i+=1
print(squareOfEvenNumber)