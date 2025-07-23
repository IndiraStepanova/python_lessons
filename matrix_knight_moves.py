#https://stepik.org/lesson/416755/step/8?unit=406263

n = 8   # шахматное поле 8*8
knight_col, knight_row = input()
matrix = [['.' for _ in range(n)] for col in range(n)]

knight_col = ord(knight_col) - ord('a')
knight_row = n - int(knight_row)

matrix[knight_row][knight_col] = 'N'

for row in range(n):
    for col in range(n):
        if abs((row - knight_row) * (col - knight_col)) == 2:
            matrix[row][col] = '*'

for row in matrix:
    print(*row)

