#https://stepik.org/lesson/334152/step/9?unit=317561

# объявление функции
def is_magic(date):
    day = int(date[:2])
    month = int(date[3:5])
    year = date[6:]
    return day * month == int(year[2:])

# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))

