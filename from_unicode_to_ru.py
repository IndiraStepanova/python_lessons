#https://stepik.org/lesson/313439/step/13?unit=295959

new_input = input().replace('[u-', '')

word = ''

#new_input = new_input.replace('[u-', '')

for symbol in new_input:
    if symbol.isdigit():
        word += symbol
    elif symbol == ']':
        word = chr(int(word))
        print(word, end='')
        word = ''
    else:
        print(symbol, end='')




