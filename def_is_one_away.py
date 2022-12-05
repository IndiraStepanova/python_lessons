"""
принимает в качестве аргументов два слова word1 и word2 и возвращает значение True если слова имеют одинаковую длину
и отличаются ровно в 1 символе и False в противном случае.

"""


# объявление функции
def is_one_away(word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        return False
    cnt = 0
    i = 0
    while i < len(word1) and cnt <= 1:
        if word1[i] != word2[i]:
            cnt += 1
        i += 1
    return cnt == 1

# считываем данные
txt1, txt2 = input(), input()

# вызываем функцию
print(is_one_away(txt1, txt2))
