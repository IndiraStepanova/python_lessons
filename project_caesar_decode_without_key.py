user_text = input().split()


# функция для декодирования
def decode_circle_shift(l, decode_l):
    if (l.isupper() and decode_l < ord('A')) or (l.islower() and decode_l < ord('a')):
        decode_l += 26
    return chr(decode_l)


for shift in range(0, 25):
    print(shift+1, end=' ')
    for word in user_text:
        decode_word = ''
        for letter in word:
            if letter.isalpha():
                decode_letter = ord(letter) - shift
                decode_word += decode_circle_shift(letter, decode_letter)
            else:
                decode_word += letter
        print(decode_word, end=' ')
    print()
