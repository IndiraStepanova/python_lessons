# https://stepik.org/lesson/416759/step/3?unit=406267

n = int(input())
matrix = [[int(num) for num in input().split()] for row in range(n)]
for row in range(n):
    for col in range(row + 1, n):
        matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
    print(*matrix[row])