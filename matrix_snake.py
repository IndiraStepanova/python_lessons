# https://stepik.org/lesson/416757/step/8?unit=406265

def print_matrix(mtrx, rows, cols, width=1):
    for r in range(rows):
        for c in range(cols):
            print(str(mtrx[r][c]).ljust(width), end=' ')
        print()


n, m = input().split()
n, m = int(n), int(m)
matrix = [[row * m + col for col in range(1, m + 1)] for row in range(n)]
for row in range(n):
    if row % 2 != 0:
        matrix[row].reverse()
print_matrix(matrix, n, m, width=2)