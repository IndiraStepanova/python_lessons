"""Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки. Программа принимает на вход две строки 
одинаковой длины, на первой строке записаны символы исходного алфавита, на второй строке — символы конечного алфавита, 
после чего идёт строка, которую нужно зашифровать переданным ключом, и ещё одна строка, которую нужно расшифровать.
Пусть, например, на вход программе передано:
abcd
*d%#
abacabadaba
#*%*d*%
Это значит, что символ a исходного сообщения заменяется на символ * в шифре, b заменяется на d, c — на % и d — на #.
Нужно зашифровать строку abacabadaba и расшифровать строку #*%*d*% с помощью этого шифра. Получаем следующие строки, 
которые и передаём на вывод программы:
*d*%*d*#*d*
dacabac"""

dict_code = {}
dict_decode = {}
first_str = input()
sec_str = input()
third_str = input() #строку нужно ЗАшифровать
four_str = input() #строку нужно РАСшифровать
for i in range(len(first_str)): #длина 1 и второй строки равны
    dict_code[first_str[i]] = sec_str[i]
    dict_decode[sec_str[i]] = first_str[i]

for symbol in third_str:
    if symbol in dict_code.keys():
        print(dict_code[symbol], end = "")
print()
for symbol in four_str:
    if symbol in dict_decode.keys():
        print(dict_decode[symbol], end = "")
    





