# https://stepik.org/lesson/416759/step/4?unit=406267

n = int(input())
matrix = [['.' for col in range(n)] for row in range(n)]
for row in range(n):
    for col in range(n):
        matrix[n // 2][col] = '*'
        matrix[row][n // 2] = '*'
        matrix[row][row] = '*'
        matrix[row][n - 1 - row] = '*'
        print(matrix[row][col], end=' ')
    print()

