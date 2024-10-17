# sum of first n natural N number those who not divisible by 2
# print 5 natural number not divisible by 
# 1, 3, 5,7,9
num = int(input("Enter number sum of n natural number not divisible by 2: "))

count = 0
current_number = 1
sumOfNutralNumber = 0

while count < num:
    if( current_number % 2 != 0):
        sumOfNutralNumber += current_number
        count+=1
    current_number+=1
print(sumOfNutralNumber)