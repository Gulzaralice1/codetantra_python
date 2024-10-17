# a program to get substring out of a string
# words = str(input("enter wors"))
# word = str(input("enter wword yo find"))
# if word in words :
#     print(word,"yes ")

# if word not in words:
#     print("word not present ")


matrix1 = [
    [1, 1, 1],
    [1, 1, 1]

]
matrix2 = [
    [2, 2, 2],
    [2, 2, 2],
    [2, 2, 2]
]

result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1)) ]

for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
        for k in range(len(matrix1[0])):
            result[i][j]+=matrix1[i][k] * matrix2[k][j]
print(result)

for row in result:
    print(row)
