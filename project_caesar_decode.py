#https://stepik.org/lesson/352860/step/8?unit=336821

user_text = input().split()


# функция для декодирования
def decode_circle_shift(l, decode_l):
    if (l.isupper() and decode_l < ord('A')) or (l.islower() and decode_l < ord('a')):
        decode_l += 26
    return chr(decode_l)


for word in user_text:
    decode_word = ''
    shift = 25  # длина сдвига
    for letter in word:
        if letter.isalpha():
            decode_letter = ord(letter) - shift
            decode_word += decode_circle_shift(letter, decode_letter)
        else:
            decode_word += letter
    print(decode_word, end=' ')







