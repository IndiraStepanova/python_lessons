'''Напишите программу, на вход которой на первой строке подаётся число nn, после этого 
на nn строках передаются числа x_ix 

Для каждого числа x на отдельной строке выведите значение f(x_i). 
Функция f(x) уже реализована и доступна для вызова. 

Функция вычисляется достаточно долго и зависит только от переданного аргумента x. 
Для того, чтобы уложиться в ограничение по времени, нужно сохранять вычисленные значения.'''

def f(x): #кабута функция
    return x+1

cnt = int(input())  
dict = {}
while cnt != 0:
    i = int(input())
    if i not in dict:
        dict[i] = f(i)
    print(dict[i])
    cnt -= 1

        