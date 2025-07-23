## https://stepik.org/lesson/416754/step/12?unit=406262
#max_num1 левее главной диагонали
'''n = int(input())
matrix = [[int(num) for num in input().split()] for row in range(n)]
max_num = matrix[0][0]
for row in range(n):
    for col in range(n):
        if row >= col:
            max_num = max(max_num, matrix[row][col])
print(max_num)
'''

"""
#https://stepik.org/lesson/416754/step/13?unit=406262
#max_num2
n = int(input())
matrix = [[int(num) for num in input().split()] for row in range(n)]
max_num = matrix[0][0]
for row in range(n):
    for col in range(n):
        if (row >= col) and (row + col + 1 <= n):    # left quater max
            max_num = max(max_num, matrix[row][col])
        elif (row <= col) and (row + col + 1 >= n):    # right quater max
            max_num = max(max_num, matrix[row][col])
print(max_num)

"""

#https://stepik.org/lesson/416759/step/2?unit=406267
#max_num3 правее побочной диагонали
n = int(input())
matrix = [[int(num) for num in input().split()] for row in range(n)]
max_num = matrix[0][0]
for row in range(n):
    for col in range(n):
        if row >= n - 1 - col:
            max_num = max(max_num, matrix[row][col])
print(max_num)
