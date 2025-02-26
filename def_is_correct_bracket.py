# объявление функции
def is_correct_bracket(text: str) -> bool:
    bracket_string = ''
    flag = True
    for bracket in text:
        if bracket == '(':
            bracket_string += bracket
        elif bracket == ')' and bracket_string != '':
            new_range = bracket_string.rfind('(')
            bracket_string = bracket_string[:new_range]
        elif bracket == ')' and bracket_string == '':
            flag = False
    if bracket_string.count('(') != 0:
        flag = False
    return flag



# считываем данные
#txt = input()

# вызываем функцию
print(is_correct_bracket('(222(oo(0)2)jo;)2'))
print(is_correct_bracket('(()())'))
print(is_correct_bracket('(())()'))
print(is_correct_bracket('()(())'))

print(is_correct_bracket('()()()'))
print(is_correct_bracket('()(())()()()(())()(()())((()))'))
print(is_correct_bracket('()(())()(()())((()))()(())'))
print(is_correct_bracket('())()()()('))

print(is_correct_bracket(')))((('))
