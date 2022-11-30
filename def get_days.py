# объявление функции
def get_days(month):
    """
      if month == 2:
        return 28
    if month in range(1, 8, 2) or month in range(8, 13, 2):
        return 31
    else:
        return 30
   """
    my_calendar = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    return my_calendar[month - 1]


# считываем данные
num = int(input())

# вызываем функцию
print(get_days(num))
