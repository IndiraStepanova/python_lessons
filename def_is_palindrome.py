"""
функция принимает в качестве аргумента строку text и
возвращает значение True если указанный текст является палиндромом и False в противном случае.
"""


# объявление функции
def is_palindrome(text: str) -> bool:
    for symbol in text:
        if symbol.isalpha() is False:
            text = text.replace(symbol, '')
    start = 0
    end = len(text) - 1
    flag = True
    while start < end and flag is True:
        if text.lower()[start] != text.lower()[end]:
            flag = False
        start += 1
        end -= 1
    return flag


# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))
