matrix1 = [
    [1,1,1],
    [1,1,1],
    [1,1,1]
]
matrix2 = [
    [2,2,2],
    [2,2,2],
    [2,2,2]
]

result = []

for i in range(len(matrix1)):  #row 1 to 3 three
    row = []
    for j in range(len(matrix2[0])):
        row.append(matrix1[i][j] + matrix2[i][j])
    result.append(row)
print(result)