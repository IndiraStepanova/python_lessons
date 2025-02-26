#https://stepik.org/lesson/334152/step/6?unit=317561
from math import factorial, ceil

# объявление функции
def compute_binom(n, k):
    return ceil(factorial(n) / (factorial(k) * factorial((n - k))))

# считываем данные
n = int(input())
k = int(input())

# вызываем функцию
print(compute_binom(n, k))