'''Напишите программу, которая считывает список чисел lst из первой строки и число x из второй строки, 
которая выводит все позиции, на которых встречается число x в переданном списке lst.

Позиции нумеруются с нуля, если число x не встречается в списке, вывести строку "Отсутствует" 
(без кавычек, с большой буквы).

Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения.'''


lst = [int(current) for current in input().split()]
x = int(input())
if x not in lst:
    print('Отсутствует')
else:
    for current in range(len(lst)):
        if lst[current] == x:
            print(current, end = ' ')

'''
lst = [int(current) for current in input().split()]
x = int(input())
index = -1
if x not in lst:
    print('Отсутствует')
else:
    for current in lst:
        index += 1
        if current == x:
            print(index, end = " ")
'''

