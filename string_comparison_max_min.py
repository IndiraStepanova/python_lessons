#https://stepik.org/lesson/1402735/step/11?unit=1419697
'''
word_max = ''
word_min = ''
word_input = ''

while word_input != 'КОНЕЦ':
    if word_min == '':
        word_min = word_input
    if word_min > word_max:
        word_max = word_min
    elif word_input > word_max:
        word_max = word_input
    elif word_input < word_min:
        word_min = word_input
    word_input = input()
'''

word_input = input()
word_max = word_input
word_min = word_input


while word_input != 'КОНЕЦ':
    if word_input < word_min:
        word_min = word_input
    if word_input > word_max:
        word_max = word_input
    word_input = input()


print(f'''Минимальная строка ⬇️: {word_min}
Максимальная строка ⬆️: {word_max}''')