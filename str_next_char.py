first_char = str(input())

next_char = chr(ord(first_char)+1)
if first_char.lower():
    print("Дальше букв нет")
else:
    print(next_char)