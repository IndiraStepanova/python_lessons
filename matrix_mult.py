#https://stepik.org/lesson/416755/step/1?unit=406263


def print_matrix(matrix, n, m, width=1):
    for r in range(n):
        for c in range(m):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


n, m = int(input()), int(input())
mult = [[row * col for col in range(m)] for row in range(n)]
print_matrix(mult, n, m, width=2)