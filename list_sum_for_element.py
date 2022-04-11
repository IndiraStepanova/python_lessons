"""Напишите программу, на вход которой подаётся список чисел одной строкой. Программа должна для каждого 
элемента этого списка вывести сумму двух его соседей. Для элементов списка, являющихся крайними, одним из соседей 
считается элемент, находящий на противоположном конце этого списка. Например, если на вход подаётся список "1 3 5 6 10", 
то на выход ожидается список "13 6 9 15 7" (без кавычек).

Если на вход пришло только одно число, надо вывести его же.

Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом."""

'''
list = [int(i) for i in input().split()]
sum = 0
if len(list) == 1:
    print(*list)
elif len(list) > 2:
    num_1 = list[1]+list[-1]
    print(num_1,end=" ")
    last_num = list[-2]+list[0]
    for i in range(1,(len(list)-1)):
        sum = list[i-1]+list[i+1]
        print(sum,end = " ")
    print(last_num)
'''
list = [int(i) for i in input().split()]
sum = []
if len(list) == 1:
    print(*list)
else:
    num_1 = list[1]+list[-1]
    sum.append(num_1)
    for i in range(1,(len(list)-1)):
        sum_for_element = list[i-1]+list[i+1]
        sum.append(sum_for_element)
    last_num = list[-2]+list[0]
    sum.append(last_num)
    print(*sum)
