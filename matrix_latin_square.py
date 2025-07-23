# https://stepik.org/lesson/416759/step/6?unit=406267

n = int(input())
matrix = [[int(num) for num in input().split()] for row in range(n)]

# Проверяем, что матрица составлена только и из всех чисел последовательности от 1 до n
def all_nums_in_row(c, m):
    all_nums = [int(num) for num in range(1, n + 1)]
    temp_list = []
    flag = True
    for row in m:
        temp_list.extend(row)
        temp_list.sort()
        if all_nums != temp_list:
            flag = False
            break
        temp_list = []
    return flag


def all_nums_in_col(c, m):
    all_nums = [int(num) for num in range(1, n + 1)]
    temp_list = []
    flag = True
    for row in range(c):
        for col in range(c):
            temp_list.append(m[col][row])
        temp_list.sort()
        if all_nums != temp_list:
            flag = False
            break
        temp_list = []
    return flag


if int(min(all_nums_in_row(n, matrix), all_nums_in_col(n, matrix))) > 0:
    print('YES')
else:
    print('NO')