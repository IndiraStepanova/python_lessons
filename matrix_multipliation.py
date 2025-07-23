# https://stepik.org/lesson/416756/step/10?unit=406264


def print_matrix(mtrx, rows, cols, width=1):
    for r in range(rows):
        for c in range(cols):
            print(str(mtrx[r][c]).ljust(width), end=' ')
        print()


n, m = input().split()
n, m = int(n), int(m)
matrix_1 = [[int(num) for num in input().split()] for row in range(n)]
input()
m, k = input().split()
m, k = int(m), int(k)
matrix_2 = [[int(num) for num in input().split()] for row in range(m)]

matrix_3 = [[0] * k for row in range(n)]

for row in range(n):
    for col in range(k):
        for i in range(m):
            matrix_3[row][col] += (matrix_1[row][i] * matrix_2[i][col])

print_matrix(matrix_3, n, k, width=1)
