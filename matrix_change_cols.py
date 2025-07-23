#https://stepik.org/lesson/416755/step/3?unit=406263

n, m = int(input()), int(input())
matrix = [[int(num) for num in input().split()] for _ in range(n)]
i, j = [int(num) for num in input().split()]


def print_matrix(matrix, n, m, width=1):
    for r in range(n):
        for c in range(m):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


for row in range(n):
    matrix[row][i], matrix[row][j] = matrix[row][j], matrix[row][i]

print_matrix(matrix, n, m, width=2)



