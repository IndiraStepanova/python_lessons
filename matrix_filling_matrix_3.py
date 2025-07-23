# https://stepik.org/lesson/416757/step/5?unit=406265

def print_matrix(mtrx, num, width=1):
    for r in range(num):
        for c in range(num):
            print(str(mtrx[r][c]).ljust(width), end=' ')
        print()


n = int(input())
matrix = [[0] * n for _ in range(n)]
for row in range(n):
    matrix[row][row] = 1
    matrix[row][n - row - 1] = 1
print_matrix(matrix, n, width=2)