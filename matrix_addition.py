# https://stepik.org/lesson/416756/step/9?unit=406264


def print_matrix(mtrx, rows, cols, width=1):
    for r in range(rows):
        for c in range(cols):
            print(str(mtrx[r][c]).ljust(width), end=' ')
        print()


n, m = input().split()
n, m = int(n), int(m)
matrix_1 = [[int(num) for num in input().split()] for row in range(n)]
input()
matrix_2 = [[int(num) for num in input().split()] for row in range(n)]

matrix_3 = [[matrix_1[row][col] + matrix_2[row][col] for col in range(m)] for row in range(n)]

print_matrix(matrix_3, n, m, width=1)
