#https://stepik.org/lesson/356380/step/14?unit=340495

from random import sample
from string import ascii_letters, ascii_lowercase, ascii_uppercase, digits

bad_symbols = 'lI1oO0'


def correct_pwd(password):
    if set(password).isdisjoint(set(ascii_lowercase)) is False:
        if set(password).isdisjoint(set(ascii_uppercase)) is False:
            if set(password).isdisjoint(set(digits)) is False:
                return True
    return False


def generate_pwd(length):
    pwd = []
    while correct_pwd(pwd) is False:
        allowed_symbols = ''.join((set(ascii_letters) | set(digits)) - set(bad_symbols))
        pwd = sample(allowed_symbols, length)
    return pwd

    
def generate_some_pwds(cnt, length):
    for _ in range(cnt):
        print(''.join(generate_pwd(length)))


n = int(input())    # кол-во паролей
m = int(input())    # длина паролей

generate_some_pwds(n, m)
