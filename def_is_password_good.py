"""
Пароль является надежным если:

его длина не менее 8 символов;
он содержит как минимум одну заглавную букву (верхний регистр);
он содержит как минимум одну строчную букву (нижний регистр);
он содержит хотя бы одну цифру.
"""
"""def is_good_password(password):
    return len(password) >= 8 \
           and not password.islower() \
           and not password.isupper() \
           and password.isalnum() \
           and not password.isdigit() \
           and not password.isalpha()
"""


def is_good_password(password):
    if len(password) < 8:
        return False
    else:
        flag1 = False
        flag2 = False
        flag3 = False
        for symbol in password:
            if symbol.islower():
                flag1 = True
            elif symbol.isupper():
                flag2 = True
            elif symbol.isdigit():
                flag3 = True
        return flag1 and flag2 and flag3


# считываем данные
pwd = input()

# вызываем функцию
print(is_good_password(pwd))

