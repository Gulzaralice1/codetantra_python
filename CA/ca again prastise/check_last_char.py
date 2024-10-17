char = input("ENete char? :.")
last = char[-1]

if last.isalpha():
    print("alpha")
elif not  last.isdigit():
    print("char")
else:
    print("digit")