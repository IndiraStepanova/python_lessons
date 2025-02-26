# https://stepik.org/lesson/349845/step/1?unit=333700

import random


def generator():
    return random.randint(1, 100)


def is_valid(n):
    return 1 <= int(n) <= 100


def start_game():
    num = generator()
    print('Добро пожаловать в числовую угадайку')
    cnt = 0
    while True:
        user_num = input('Введите число от 1 до 100: ')
        if user_num.isdigit() and is_valid(user_num):
            user_num = int(user_num)
            if user_num < num:
                cnt += 1
                print('Ваше число меньше загаданного, попробуйте еще разок')
            elif user_num > num:
                cnt += 1
                print('Ваше число больше загаданного, попробуйте еще разок')
            else:
                cnt += 1
                print('Вы угадали, поздравляем!')
                print('Количество попыток:', cnt)
                print('Хотите сыграть еще? (д/н)')
                again()
                break
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')
            cnt += 1


def again():
    answer = input()
    if answer in 'дн':
        if answer == 'д':
            start_game()
        else:
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
    else:
        print('Введите "д" или "н"')
        return again()


start_game()

