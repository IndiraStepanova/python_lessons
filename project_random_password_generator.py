#https://stepik.org/lesson/349848/step/1?unit=333703


import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
bad_symbols = 'il1Lo0O'
chars = ''
approval = 'д'

# считывание пользовательских данных:
cnt_pswds = int(input('Укажите количество паролей для генерации: '))
lenght_pswd = int(input('Укажите длину одного пароля: '))
digits_on = input('Включать ли цифры 0123456789? д/н ')
uppercase_on = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? д/н ')
lowercase_on = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? д/н ')
punctuation_on = input('Включать ли символы !#$%&*+-=?@^_? д/н ')
bad_symbols_off = input('Исключать ли неоднозначные символы il1Lo0O? д/н ')


# Функция исключения определенного набора символов:
def delete_chars(string, chars):
    for e in string:
        if e in chars:
            string = string.replace(e, '')
    return string


# Функция генерации пароля:
def generate_password(length, chars):
    pswd = random.sample(chars, length)
    pswd = ''.join(pswd)
    return pswd


# Настройка генерируемых паролей:
if digits_on.lower() == approval:
    chars += digits
if uppercase_on.lower() == approval:
    chars += uppercase_letters
if lowercase_on.lower() == approval:
    chars += lowercase_letters
if punctuation_on.lower() == approval:
    chars += punctuation
if bad_symbols_off.lower() == approval:
    delete_chars(chars, bad_symbols)

# Генерация нужного количества паролей согласно пользовательским данным:
for password in range(cnt_pswds):
    password = generate_password(lenght_pswd, chars)
    print(password)

