'''
letters_cnt = 26
alphabet = []
cnt = 1
for letter in range(97, 97 + letters_cnt):
    alphabet.append(chr(letter) * cnt)
    cnt += 1
print(alphabet)
'''
letters_cnt = 26
alphabet = []
for letter in range(letters_cnt):
    alphabet.append(chr(ord('a') + letter) * (letter + 1))
print(alphabet)