# https://stepik.org/lesson/416754/step/14?unit=406262

n = int(input())
matrix = [[int(num) for num in input().split()] for row in range(n)]
upper_quater = 0
right_quater = 0
lower_quater = 0
left_quater = 0
for row in range(n):
    for col in range(n):
        if (row > col) and (row + col + 1 < n):    # left quater sum
            left_quater += matrix[row][col]
        elif (row < col) and (row + col + 1 < n):  # upper quater sum
            upper_quater += matrix[row][col]
        elif (row < col) and (row + col + 1 > n):    # right quater sum
            right_quater += matrix[row][col]
        elif (row > col) and (row + col + 1 > n):    # lower quater sum
            lower_quater += matrix[row][col]

print(f'''Верхняя четверть: {upper_quater}
Правая четверть: {right_quater}
Нижняя четверть: {lower_quater}
Левая четверть: {left_quater}''')
