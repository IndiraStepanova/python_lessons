#https://stepik.org/lesson/334152/step/8?unit=317561

"""
from datetime import datetime
import locale


# объявление функции
def get_month(language, number):
    if language == 'ru':
        locale.setlocale(locale.LC_TIME, 'ru')
    return datetime.strptime(str(number), "%m").strftime("%B").lower()


# считываем данные
lan = input()
num = int(input())

# вызываем функцию
print(get_month(lan, num))
"""

# объявление функции
def get_month(language, number):
    lng_ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь',
              'декабрь']
    lng_en = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
              'november', 'december']

    if language == 'ru':
        return lng_ru[number-1]
    elif language == 'en':
        return lng_en[number-1]


# считываем данные
lan = input()
num = int(input())

# вызываем функцию
print(get_month(lan, num))
