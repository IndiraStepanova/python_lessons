# https://stepik.org/lesson/416756/step/11?unit=406264


def print_matrix(mtrx, rows, cols, width=1):
    for r in range(rows):
        for c in range(cols):
            print(str(mtrx[r][c]).ljust(width), end=' ')
        print()


n = int(input())
matrix = [[int(num) for num in input().split()] for row in range(n)]
m = int(input())
matrix_result = matrix
temp_matrix = [[0] * n for row in range(n)]
cnt = 0


def exp_matrix(my_matrix, j, m_temp, m_result):
    for row in range(j):
        for col in range(j):
            for i in range(j):
                m_temp[row][col] += (m_result[row][i] * my_matrix[i][col])


while cnt != (m - 1):
    exp_matrix(matrix, n, temp_matrix, matrix_result)
    matrix_result = temp_matrix
    temp_matrix = [[0] * n for row in range(n)]
    cnt += 1

print_matrix(matrix_result, n, n, width=1)
