first_string = str(input())
second_string = str(input())


def clean_string(s):
    for i in s:
        if not i.isalpha():
            s = s.replace(i, '')
    return s


first_string = clean_string(first_string)


second_string = clean_string(second_string)


if first_string.isalpha and second_string.isalpha:
    if first_string.lower() == second_string.lower():
        print('YES')
    else:
        print('NO')
else:
    print('NO')

