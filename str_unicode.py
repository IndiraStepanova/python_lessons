'''
a, b = int(input()), int(input()) # находим символы в диапазоне [a, b]
for char in range(a, b+1):
    print(chr(char), end=' ')
'''
a = input() # переводим в число символы из строки
for char in a:
    print(ord(char), end=' ')