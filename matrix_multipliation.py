def print_matrix(mtrx, rows, cols, width=1):
    for r in range(rows):
        for c in range(cols):
            print(str(mtrx[r][c]).ljust(width), end=' ')
        print()


n, m = input().split()
n, m = int(n), int(m)
matrix = [[0] * m for _ in range(n)]
cnt = 0

up = 0    # верхняя строка
right = m - 1   # правый столбец
low = n - 1  # нижняя строка
left = 0    # левый столбец

for circle in range((min(n, m)+1)//2):
    for col in range(left, right):
        cnt += 1
        matrix[up][col] = cnt
    for row in range(up, low + 1):
        cnt += 1
        matrix[row][right] = cnt
    if cnt == n * m:
        break
    for col in range(left, right)[::-1]:
        cnt += 1
        matrix[low][col] = cnt
    for row in range(up + 1, low)[::-1]:
        cnt += 1
        matrix[row][left] = cnt
    up += 1
    right -= 1
    low -= 1
    left += 1
print_matrix(matrix, n, m, width=2)

