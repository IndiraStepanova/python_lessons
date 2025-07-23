# https://stepik.org/lesson/416757/step/7?unit=406265

def print_matrix(mtrx, rows, cols, width=1):
    for r in range(rows):
        for c in range(cols):
            print(str(mtrx[r][c]).ljust(width), end=' ')
        print()


n, m = input().split()
n, m = int(n), int(m)
matrix = [[(col + row) % m + 1 for col in range(m)] for row in range(n)]
print_matrix(matrix, n, m, width=2)