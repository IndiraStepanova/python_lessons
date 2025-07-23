# https://stepik.org/lesson/416755/step/7?unit=406263

n = int(input())
matrix = [[int(num) for num in input().split()] for row in range(n)]
# 3
# 1 2 3
# 4 5 6
# 7 8 9

for row in range(n)[::-1]:
    for col in range(n)[::-1]:
        print(str(matrix[col][n - row - 1]).ljust(1), end=' ')
    print()

# 7 4 1
# 8 5 2
# 9 6 3


