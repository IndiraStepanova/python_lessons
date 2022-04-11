'''Недавно мы считали для каждого слова количество его вхождений в строку. Но на все слова может быть 
не так интересно смотреть, как, например, на наиболее часто используемые.

Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит самое 
частое слово в этом тексте и через пробел то, сколько раз оно встретилось. Если таких слов несколько, 
вывести лексикографически первое (можно использовать оператор < для строк).

В качестве ответа укажите вывод программы, а не саму программу.

Слова, написанные в разных регистрах, считаются одинаковыми.'''
dict= {}
max_count = -1
max_word = " "
with open('D:\\python\\dataset_pyhon\\dataset_3363_3 (2).txt', 'r') as inf:
    for line in inf:
        #print(line.lower().strip().split(" "))
        for word in line.lower().strip().split(" "):
            if word in dict:
                dict[word] += 1
            else:
                dict[word] = 1
for key, value in dict.items():
    if value > max_count:
        max_count = value
        max_word = key
    elif value == max_count and key > max_word:
        max_word = key
print(max_word, max_count, sep = " ")