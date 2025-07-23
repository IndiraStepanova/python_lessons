#https://stepik.org/lesson/416755/step/2?unit=406263
n, m = int(input()), int(input())
matrix = [[int(num) for num in input().split()] for row in range(n)]
r, c = 0, 0
for row in range(n):
    for col in range(m):
        if matrix[r][c] < matrix[row][col]:
            r = row
            c = col
print(r, c)