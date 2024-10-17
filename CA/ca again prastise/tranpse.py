matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
num_row = len(matrix)
num_col = len(matrix[0])
transposed_matrix = [[0] * num_row for _ in range(num_col)]
transposed_matrix = [[0] * num_row for _ in range(num_col)]
for i in range(num_row):
    for j in range(num_col):
        transposed_matrix[j][i] = matrix[i][j]

for row in transposed_matrix:
    print(row)

