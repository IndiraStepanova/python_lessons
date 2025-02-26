#https://stepik.org/lesson/334152/step/7?unit=317561

words_before_twenty = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять',
         'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать',
         'восемнадцать', 'девятнадцать']

words_after_twenty = ['двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']

# объявление функции
def from_1_to_19(n):
    return words_before_twenty[n - 1]


def full_first_part(n):
    return words_after_twenty[n // 10 - 2]


def full_second_part(n):
    return words_before_twenty[n % 10 - 1]


def number_to_words(num):
    first_part = ''
    sec_part = ''
    if num <= 19:
        first_part = from_1_to_19(num)
    elif num in [20, 30, 40, 50, 60, 70, 80, 90]:
        first_part = full_first_part(num)
    else:
        first_part = full_first_part(num)
        sec_part = full_second_part(num)
    return f'{first_part} {sec_part}'.rstrip()


# считываем данные
n = int(input())

# вызываем функцию
print(number_to_words(n))