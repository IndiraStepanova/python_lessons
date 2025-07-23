# https://stepik.org/lesson/416757/step/4?unit=406265

def print_matrix(mtrx, rows, cols, width=1):
    for r in range(rows):
        for c in range(cols):
            print(str(mtrx[r][c]).ljust(width), end=' ')
        print()


n, m = input().split()
n = int(n)
m = int(m)
matrix = [[col * n + row for col in range(m)] for row in range(1, n + 1)]
print_matrix(matrix, n, m, width=2)
# 1  4  7  10 13
# 2  5  8  11 14
# 3  6  9  12 15