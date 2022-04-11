"""Узнав, что ДНК не является случайной строкой, только что поступившие в Институт биоинформатики 
студенты группы информатиков предложили использовать алгоритм сжатия, который сжимает повторяющиеся символы в строке.

Кодирование осуществляется следующим образом:
s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы одинаковых символов исходной строки заменяются 
на этот символ и количество его повторений в этой позиции строки.

Напишите программу, которая считывает строку, кодирует её предложенным алгоритмом и выводит закодированную 
последовательность на стандартный вывод. Кодирование должно учитывать регистр символов."""


s = input()
cnt = 0
previous = '@'
for current in s:
    if cnt == 0:
        previous = current
    if current == previous:
        cnt+=1
    else:
        print(previous,cnt,sep ="",end = "")
        previous = current
        cnt = 1
print(previous,cnt,sep ="",end = "")


""""genome = input()+' 'добавляется пробел в конце, чтобы не нужно было отдельно обрабатывать последний символ оригинальной строки
s = 0
n=genome[0]
for i in genome:       
    if n!=i:
        print(n + str(s), end = '')
        s=0
        n=i
    s+=1
"""