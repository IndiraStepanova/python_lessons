def is_prime_number(number):
    cnt = 0
    if number == 1:
        return False
    else:
        for factor in range(2, number):
            if number % factor == 0:
                return False
        return True


def get_next_prime(n):
    n += 1
    while not is_prime_number(n):
        n += 1
    return n


# считываем данные
num = int(input())

# вызываем функцию
print(get_next_prime(num))