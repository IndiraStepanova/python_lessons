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
# pwd = input()

# вызываем функцию
print(is_good_password('aaAA12qqp'))
print(is_good_password('aa13AN'))
print(is_good_password('aaaaaaaaaaaaa'))
print(is_good_password('AAAAAAAAAAA'))
print(is_good_password('734638763978653'))
print(is_good_password('AAPPqq9S'))
print(is_good_password('AABBccssss'))
print(is_good_password('AA23423423'))
print(is_good_password('dsas233232232'))
print(is_good_password('99yyPPgg'))
print(is_good_password('99yyPPg'))
print(is_good_password('()+_№;%:'))
print(is_good_password('        '))
print(is_good_password('aaaaaaA@'))
