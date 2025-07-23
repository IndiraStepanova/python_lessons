# https://stepik.org/lesson/416757/step/6?unit=406265

def print_matrix(mtrx, num, width=1):
    for r in range(num):
        for c in range(num):
            print(str(mtrx[r][c]).ljust(width), end=' ')
        print()


def is_upper_lower_quater(num, r, c):
    return ((r <= c) and (r + c + 1 <= n)) or ((r >= c) and (r + c + 1 >= n))


n = int(input())
matrix = [[0] * n for _ in range(n)]
for row in range(n):
    for col in range(n):
        if is_upper_lower_quater(n, row, col):
            matrix[row][col] = 1
print_matrix(matrix, n, width=2)