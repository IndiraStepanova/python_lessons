#https://stepik.org/lesson/356380/step/13?unit=340495
from random import sample
from string import ascii_letters, digits

bad_symbols = 'lI1oO0'

def generate_pwd(length, ):
    allowed_symbols = ''.join((set(ascii_letters) | set(digits)) - set(bad_symbols))
    return sample(allowed_symbols, length)


def generate_some_pwds(cnt, length):
    for _ in range(cnt):
        print(''.join(generate_pwd(length)))


n = int(input())    # кол-во паролей
m = int(input())    # длина паролей

generate_some_pwds(n, m)
