num = int(input("enter number: "))

a,b = 0,1

print("a",a)
print("b",b)

for i in range(2,num):
    a,b= b,a+b
    print(b)
