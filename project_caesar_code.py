#https://stepik.org/lesson/352860/step/10?unit=336821

user_text = input().split()


# функция для подсчета длины сдвига без знаков препинания
def shift_len(w):
    s = 0
    for l in w:
        if l.isalpha():
            s += 1
    return s


# функция для кодирования
def code_circle_shift(letter, code_l):
    if (letter.isupper() and code_l > ord('Z')) or (l.islower() and code_l > ord('z')):
        code_l -= 26
    return chr(code_l)


for word in user_text:
    code_word = ''
    shift = shift_len(word)    # длина сдвига
    for letter in word:
        if letter.isalpha():
            code_letter = ord(letter) + shift
            code_word += code_circle_shift(letter, code_letter)
        else:
            code_word += letter
    print(code_word, end=' ')







