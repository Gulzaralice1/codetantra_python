matrix1 = [
    [1, 1, 1],
    [1, 1, 1]

]
matrix2 = [
    [2, 2, 2],
    [2, 2, 2],
    [2, 2, 2]
]

# Initialize the result matrix with zeros
result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]

# Perform matrix multiplication
for i in range(len(matrix1)):  # Iterate through rows of matrix1
    for j in range(len(matrix2[0])):  # Iterate through columns of matrix2
        for k in range(len(matrix1[0])):  # Iterate through rows of matrix2 (or columns of matrix1)
            result[i][j] += matrix1[i][k] * matrix2[k][j]

# Print the result matrix
for row in result:
    print(row)
