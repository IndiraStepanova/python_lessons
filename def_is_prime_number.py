def is_prime_number(number: int) -> bool:
    cnt = 0
    if number == 1:
        return False
    else:
        for factor in range(2, number):
            if number % factor == 0:
                return False
        return True


# считываем данные
num = int(input())

# вызываем функцию
print(is_prime_number(num))
