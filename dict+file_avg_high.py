"""Дан файл с таблицей в формате TSV с информацией о росте школьников разных классов.
Напишите программу, которая прочитает этот файл и подсчитает для каждого класса средний рост учащегося.
Файл состоит из набора строк, каждая из которых представляет собой три поля:
Класс Фамилия Рост
Класс обозначается только числом. Буквенные модификаторы не используются. Номер класса может быть от 1 до 11 включительно. В фамилии нет пробелов, а в качестве роста используется натуральное число, но при подсчёте среднего требуется вычислить значение в виде вещественного числа.
Выводить информацию о среднем росте следует в порядке возрастания номера класса (для классов с первого по одиннадцатый).
 Если про какой-то класс нет информации, необходимо вывести напротив него прочерк """

'''
dict_classes = {}
classes = 11
line = []
with open('D:\\python\\dataset_pyhon\\dataset_3380_5.txt', 'r') as inf:
    for string in inf:
        line = string.strip().split("\t")
        class_num, high = int(line[0]), int(line[2])
        if class_num not in dict_classes.keys():
            dict_classes[class_num] = [high] #создается список и в него добавляется элемент с типом строка
        else:
            dict_classes[class_num].append(high)
for i in range(1, classes+1):
    if i in dict_classes.keys():
        print(i, sum(dict_classes[i])/len(dict_classes[i]), sep = "\t")
    else:
        print(i, '-', sep = "\t")
'''

classes = 11
dict_classes = {int(i):[] for i in range(1,classes+1)}
with open('D:\\python\\dataset_pyhon\\dataset_3380_5.txt', 'r') as inf:
    for string in inf:
        string = string.strip().split("\t")
        class_num, high = int(string[0]), int(string[2])
        dict_classes[class_num].append(high)
for key, value in dict_classes.items():
    if len(value) > 0:
        print(key, sum(value)/ len(value), sep = '\t')
    else:
        print(key, '-', sep = '\t')
