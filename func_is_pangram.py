#https://stepik.org/lesson/334152/step/10?unit=317561

def is_pangram(text):
    for i in range(ord('a'), ord('z') + 1):
        if chr(i) not in text.lower():
            return False
    else:
        return True



# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))


