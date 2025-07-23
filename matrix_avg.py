# https://stepik.org/lesson/416754/step/11?unit=406262

def count_avg(my_row: list):
    return sum(my_row) / len(my_row)


n = int(input())
matrix = [[int(num) for num in input().split()] for row in range(n)]
cnt = 0
for row in matrix:
    row_avg = count_avg(row)
    cnt = 0
    for num in row:
        if num > row_avg:
            cnt += 1
    print(cnt)





