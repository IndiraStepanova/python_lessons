#https://stepik.org/lesson/416759/step/3?unit=406267

n = 8   # шахматное поле 8*8
queen_col, queen_row = input()
matrix = [['.' for _ in range(n)] for col in range(n)]

queen_col = ord(queen_col) - ord('a')
queen_row = n - int(queen_row)

matrix[queen_row][queen_col] = 'Q'

for row in range(n):
    for col in range(n):
        if (abs(queen_row - row) == abs(queen_col - col)) or (row == queen_row) or col == queen_col:
            matrix[row][col] = '*'
matrix[queen_row][queen_col] = 'Q'


for row in matrix:
    print(*row)
