"""Простейшая система проверки орфографии может быть основана на использовании списка известных слов.
Если введённое слово не найдено в этом списке, оно помечается как "ошибка".

Попробуем написать подобную систему.

На вход программе первой строкой передаётся количество d известных нам слов, после чего на  d 
строках указываются эти слова. Затем передаётся количество  l строк текста для проверки, после чего  l строк текста.

Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра."""
cnt_errors = 0
some_dict_of_words = []
text_str_cnt = 0
text_for_check = []
set_of_errors = set()

words_in_dict = int(input())
while cnt_errors < words_in_dict:
    word = input()
    some_dict_of_words.append(word.lower())
    cnt_errors += 1

words_in_text = int(input())
while text_str_cnt < words_in_text:
    text_for_check = [str(text).lower() for text in input().split(' ')]
    text_str_cnt += 1
    for text in text_for_check:
        if text not in some_dict_of_words:
            set_of_errors.add(text)
print(*set_of_errors, sep = '\n')
    

