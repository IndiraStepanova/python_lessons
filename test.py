n = int(input())
matrix = [[0] * n for _ in range(n)]
for row in range(n):
    for col in range(n):
        matrix[row][col] = matrix[col][row] = abs(col - row)

for row in matrix:
    print(*row)
