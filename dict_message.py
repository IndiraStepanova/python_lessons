#https://stepik.org/lesson/488830/step/15?unit=480066

my_dict = {
    '1': '.,?!:',
    '2': 'ABC',
    '3': 'DEF',
    '4': 'GHI',
    '5': 'JKL',
    '6': 'MNO',
    '7': 'PQRS',
    '8': 'TUV',
    '9': 'WXYZ',
    '0': ' '
}
my_string = input().upper()

for symbol in my_string:
    for key, value in my_dict.items():
        if symbol in value:
            cnt = value.index(symbol) + 1
            print(key * cnt, end="")

