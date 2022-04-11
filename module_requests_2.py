"""Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".
Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.
Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/
Загрузите содержимое ﻿последнего файла из набора, как ответ на это задание."""

import requests
with open('D:\\python\\dataset_pyhon\\dataset_3378_3.txt', 'r') as indoor:
    file_address = indoor.readline().strip()
r = requests.get(file_address)
while "We" not in r.text:
    r = requests.get("https://stepic.org/media/attachments/course67/3.6.3/"+r.text)
print(r.text)