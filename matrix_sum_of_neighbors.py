'''
Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк, 
заканчивающихся строкой, содержащей только строку "end" (без кавычек)

Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме элементов 
первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1). У крайних символов соседний элемент находится 
с противоположной стороны матрицы. #найти сумму соседних элементов по горизонтали и вертикали

В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.
'''

matrix = []
string = input()
sum_of_elem = 0
while string != 'end':
    matrix.append([int(row) for row in string.split()])
    string = input()
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        upper_num = matrix[row-1][col]
        if (col == len(matrix[row]) - 1):
            right_num = matrix[row][0] 
        else:
            right_num = matrix[row][col+1]
        if (row == len(matrix) - 1):
            bottom_num = matrix[0][col]  
        else:
            bottom_num = matrix[row+1][col]
        left_num = matrix[row][col-1]
        sum_of_elem = upper_num + right_num + bottom_num + left_num
        print(sum_of_elem, end = ' ')
    print()  
'''

else:
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            upper_num = matrix[row-1][col]
            right_num = matrix[row][0] if (col == len(matrix[row]) - 1) else matrix[row][col+1] 
            
            #если условие if вверно, то выполняется вычисление слева, если нет, то справа

            bottom_num = matrix[0][col] if (row == len(matrix) - 1) else matrix[row+1][col]
            left_num = matrix[row][col-1]
            sum_of_elem = upper_num + right_num + bottom_num + left_num
            print(sum_of_elem, end = ' ')
        print()
'''