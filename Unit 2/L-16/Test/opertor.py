num1 = int(input("Enter number: "))
num2 = int(input("Enter number: "))
# operator = input("enter operator: ")
operator = input("").strip()
if operator == "==":
    print(num1 == num2)
elif operator == "!=":
    print(num1 != num2)
elif operator == ">":
    print(num1 > num2)
elif operator == ">=":
    print(num1 < num2)
elif operator == "!=":
    print(num1 <= num2)
else:
    print("invalid")
    
