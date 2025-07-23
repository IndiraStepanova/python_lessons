# https://stepik.org/lesson/416757/step/9?unit=406265


def print_matrix(mtrx, rows, cols, width=1):
    for r in range(rows):
        for c in range(cols):
            print(str(mtrx[r][c]).ljust(width), end=' ')
        print()


n, m = input().split()
n, m = int(n), int(m)
matrix = [[0] * m for _ in range(n)]
num = 0
for diagonal in range(n + m - 1):
    for row in range(n):
        for col in range(m):
            if row + col == diagonal:
                num += 1
                matrix[row][col] = num

print_matrix(matrix, n, m, width=2)