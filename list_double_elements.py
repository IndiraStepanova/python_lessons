'''
Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в одну строку значения, 
которые повторяются в нём более одного раза
'''

#моя гордость!:
a = [int(current) for current in input().split()]
previous = a[0]
new_list = []
for current in sorted(a):
    if a. count(current)>1 and current == previous and previous not in new_list:
        new_list.append(previous)
    else:  
        previous = current
print(*new_list)

#или так:
'''
a = [int(current) for current in input().split()]
a.sort()
previous = a[0]
cnt = 0
for current in a[1:]:
    if current == previous:
        cnt += 1
    else:
        previous = current
        cnt = 0
    if cnt == 1:
        print(previous, end = " ")
'''
''' 
a = [int(current) for current in input().split()]
a.sort()
previous = a[0]
same_name = False
for current in a[1:]:
    if current == previous:
        same_name = True
    else:
        previous = current
        same_name = False
    if same_name:
        print(previous, end = " ")
'''
"""
s = input().split()
print (*(i for i in set(s) if s.count(i) > 1))
"""


