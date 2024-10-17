# take two N and K rise power N^k 4
# sum of n+k
# substract sum of nk and power
n = int(input("Enter number N: "))
k = int(input("Enter number k: "))
power = n**k
add = n+k
total = power - add
print(total)

if total < 10 :
    print("Good")
elif total == 10 :
    print("better")
else:
    print("best")