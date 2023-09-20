# Matrix Diagonal Sum
# Given a square matrix mat, return the sum of the matrix diagonals.
# Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.
mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

mat = [[1, 1, 1, 1],
       [1, 1, 1, 1],
       [1, 1, 1, 1],
       [1, 1, 1, 1]]

row_length = len(mat[0])
sum = 0
for i in range(row_length):
    for j in range(row_length):
        if i == j or i+j == row_length-1:
            sum += mat[i][j]

print(sum)
