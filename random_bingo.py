#https://stepik.org/lesson/356380/step/11?unit=340495

from random import sample

def print_matrix(m, num, width=1):
    for r in range(num):
        for c in range(num):
            print(str(m[r][c]).ljust(width), end=' ')
        print()


n = 5
bingo_nums = sample(range(1, 76), 25)
bingo_matrix = [[bingo_nums.pop() for i in range(n)] for j in range(n)]
bingo_matrix[2][2] = 0
print_matrix(bingo_matrix, n, width=2)
