"""Напишите программу, которая подключает модуль math и, используя значение числа pi π  из этого модуля, находит 
для переданного ей на стандартный ввод радиуса круга периметр этого круга и выводит его на стандартный вывод."""

from math import pi
def perimetr(r):
    return 2*pi*r
r = float(input())
P = perimetr(r)
print(P)


