'''
# https://stepik.org/lesson/416755/step/4?unit=406263
# матрица симметрична относительно ГЛАВНОЙ диагонали

n = int(input())
matrix = [[int(num) for num in input().split()] for row in range(n)]
flag = 'YES'
for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            flag = 'NO'
print(flag)
'''
# https://stepik.org/lesson/416759/step/5?unit=406267
# матрица симметрична относительно побочной диагонали
n = int(input())
matrix = [[int(num) for num in input().split()] for row in range(n)]
flag = 'YES'
for row in range(n):
    for col in range(n):
        if matrix[row][col] != matrix[n - 1 - col][n - 1 - row]:
            flag = 'NO'
print(flag)