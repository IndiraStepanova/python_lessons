"""
принимает в качестве аргумента строку в «верблюжьем регистре» и преобразует его в «змеиный регистр».
"""


# объявление функции
def convert_to_python_case(text: str) -> str:
    for symbol in text:
        if symbol.isupper():
            text = text.replace(symbol, '_' + symbol.lower())
    return text


# считываем данные
# txt = input()

# вызываем функцию
print(convert_to_python_case('ConvertToInt32'))
