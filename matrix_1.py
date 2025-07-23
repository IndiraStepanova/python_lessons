
'''
# matrix_1
# https://stepik.org/lesson/416754/step/8?unit=406262
n, m = int(input()), int(input())
for i in range(n):
    for j in range(m):
        my_string = input()
        print(my_string, end=' ')
    print()
'''
# matrix_2
# https://stepik.org/lesson/416754/step/9?unit=406262
n, m = int(input()), int(input())
matrix = [[input() for col in range(m)] for row in range(n)]
for row in range(n):
    for col in range(m):
        print(matrix[row][col], end=' ')
    print()
print()
for col in range(m):
    for row in range(n):
        print(matrix[row][col], end=' ')
    print()
