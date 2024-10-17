# You are given the lengths of four sides. Your task is to check whether a rectangle can be formed
# using the given four sides, if yes, print "possible" else print "not possible".
side1 = int(input("Enter side 1: "))
side2 = int(input("Enter side 2: "))
side3 = int(input("Enter side 3: "))
side4 = int(input("Enter side 4: "))
if side1 == side3 and side2 == side4:
    print("Rectangle: ")
else:
    print("not Rectangle ")
