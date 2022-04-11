"""Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя набор строк, где в каждой строке 
записана следующая информация:
Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку
Поля внутри строки разделены точкой с запятой, оценки — целые числа.
Напишите программу, которая считывает файл с подобной структурой и для каждого абитуриента выводит его среднюю оценку 
по этим трём предметам на отдельной строке, соответствующей этому абитуриенту.
Также в конце файла, на отдельной строке, через пробел запишите средние баллы по математике, физике и русскому языку 
по всем абитуриентам.
В качестве ответа на задание прикрепите полученный файл со средними оценками.
Примечание. Для разбиения строки на части по символу ';' можно использовать метод split следующим образом:
print('First;Second-1 Second-2;Third'.split(';'))
# ['First', 'Second-1 Second-2', 'Third']"""

list = []
sum_for_first_course = 0
sum_for_second_course = 0
sum_for_third_course = 0
count_of_course = 0
sum_for_student = 0
with open('D:\\python\\dataset_pyhon\\dataset_3363_4.txt', 'r') as inf:
    for line in inf:
        list = line.strip().split(';')
        sum_for_first_course += int(list[1])
        sum_for_second_course += int(list[2])
        sum_for_third_course += int(list[3])
        count_of_course += 1
        sum_for_student = int(list[1]) + int(list[2]) + int(list[3])
        print(sum_for_student/3)
    print(sum_for_first_course/count_of_course, sum_for_second_course/count_of_course, sum_for_third_course/count_of_course)
        

        
            