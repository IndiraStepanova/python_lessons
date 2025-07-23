# https://stepik.org/lesson/416757/step/2?unit=406265


def print_matrix(m, num, width=1):
    for r in range(num):
        for c in range(num):
            print(str(m[r][c]).ljust(width), end=' ')
        print()


n = int(input())
matrix = [[0] * n for _ in range(n)]
for row in range(n):
    for col in range(n):
        if row + col + 1 < n:
            matrix[row][col] = 0
        elif col + row + 1 > n:
            matrix[row][col] = 2
    matrix[row][n - row - 1] = 1
print_matrix(matrix, n, width=1)
