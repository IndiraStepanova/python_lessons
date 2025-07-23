# https://stepik.org/lesson/416755/step/9?unit=406263

n = int(input())
matrix = [[int(num) for num in input().split()] for row in range(n)]
row_sum = 0
col_sum = 0
main_diagonal_sum = 0
secondary_diagonal_sum = 0
flag = 'YES'
new_list = list()

# Проверяем, что матрица составлена только и из всех чисел последовательности от 1 до n**2
def all_nums_in_matrix(c, m):
    all_nums = [int(num) for num in range(1, c**2 + 1)]
    our_nums = []
    for row in m:
        our_nums.extend(row)
    our_nums.sort()
    return all_nums == our_nums


# Cчитаем суммы строк, столбцов, диагоналей:
if all_nums_in_matrix(n, matrix):
    for row in range(n):
        main_diagonal_sum += matrix[row][row]
        secondary_diagonal_sum += matrix[row][n - row - 1]
        for col in range(n):
            row_sum += matrix[row][col]
            col_sum += matrix[col][row]
        new_list.append(row_sum)
        new_list.append(col_sum)
        row_sum = 0
        col_sum = 0
    new_list.append(main_diagonal_sum)
    new_list.append(secondary_diagonal_sum)
    # Сортируем и проверяем, что все числа в списке с суммами равны:
    new_list.sort()
    if new_list[0] != new_list[-1]:
        flag = 'NO'
else:
    flag = 'NO'
print(flag)




