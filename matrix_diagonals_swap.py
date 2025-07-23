# https://stepik.org/lesson/416755/step/5?unit=406263


def print_matrix(matrix, n, width=1):
    for r in range(n):
        for c in range(n):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


n = int(input())
matrix = [[int(num) for num in input().split()] for row in range(n)]

for col in range(n):
    matrix[col][col], matrix[n - col - 1][col] = matrix[n - col - 1][col], matrix[col][col]

print_matrix(matrix, n, width=1)
