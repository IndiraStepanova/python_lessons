# объявление функции
def is_correct_bracket(text):
    cnt = 0
    for bracket in text:
        if bracket == '(':
            cnt += 1
        elif bracket == ')':
            cnt -= 1
    return cnt

# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))