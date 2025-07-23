#https://stepik.org/lesson/415554/step/11?unit=405083

word = input() + ' запретил букву'

for symbol in range(ord('а'), ord('я') + 1):
    if chr(symbol) in word:
        print(word, chr(symbol))
        word = word.replace(chr(symbol), '').replace('  ', ' ').strip()
