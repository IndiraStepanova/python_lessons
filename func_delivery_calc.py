#https://stepik.org/lesson/334152/step/5?unit=317561


# объявление функции
def get_shipping_cost(quantity):
    first_good = 1000
    next_good = 120
    return first_good + next_good * (quantity-1)


# считываем данные
n = int(input())

# вызываем функцию
print(get_shipping_cost(n))