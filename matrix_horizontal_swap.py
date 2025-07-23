# https://stepik.org/lesson/416755/step/6?unit=406263

n = int(input())
matrix = [[int(num) for num in input().split()] for row in range(n)]
for row in range(n//2):
    matrix[row], matrix[n - row - 1] = matrix[n - row - 1], matrix[row]
for row in matrix:
    print(*row)


