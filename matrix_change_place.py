# https://stepik.org/lesson/416757/step/7?unit=406265

def print_matrix(mtrx, num, width=1):
    for r in range(num):
        for c in range(num):
            print(str(mtrx[r][c]).ljust(width), end=' ')
        print()


n = int(input())
matrix = [int(num) for num in range(n)] for row in range(n)]
for row in range(n):
    for col in range(n):
        if is_upper_lower_quater(n, row, col):
            matrix[row][col] = 1
print_matrix(matrix, n, width=2)