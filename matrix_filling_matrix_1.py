# https://stepik.org/lesson/416757/step/3?unit=406265

def print_matrix(mtrx, rows, cols, width=1):
    for r in range(rows):
        for c in range(cols):
            print(str(mtrx[r][c]).ljust(width), end=' ')
        print()


n, m = input().split()
n = int(n)
m = int(m)
matrix = [[row * m + col for col in range(1, m + 1)]for row in range(n)]
print_matrix(matrix, n, m, width=2)

# 1  2  3  4  5
# 6  7  8  9  10
# 11 12 13 14 15