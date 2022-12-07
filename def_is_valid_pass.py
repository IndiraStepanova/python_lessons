# объявление функции палиндром
def is_palindrome(number: str) -> bool:
    start = 0
    end = len(number) - 1
    flag = True
    while start < end and flag is True:
        if number.lower()[start] != number.lower()[end]:
            flag = False
        start += 1
        end -= 1
    return flag


# объявление функции простое число
def is_prime_number(number: int) -> bool:
    cnt = 0
    if number == 1:
        return False
    else:
        for factor in range(2, number):
            if number % factor == 0:
                return False
        return True


# объявление функции четное число
def is_even_number(number: int) -> bool:
    return number % 2 == 0


# объявление функции валидный пароль
def is_valid_password(password):
    if password.count(':') == 2:
        first_num = password[:password.find(':')]
        second_num = int(password[password.find(':') + 1:password.rfind(':')])
        third_num = int(password[password.rfind(':') + 1:])
        return is_palindrome(first_num) and is_prime_number(second_num) and is_even_number(third_num)
    return False


# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))
