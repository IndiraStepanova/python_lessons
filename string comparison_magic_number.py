#https://stepik.org/lesson/1402735/step/12?unit=1419697

word_max = ''
word_min = ''
word_input = ''
cnt = 0
for _ in range(4):
    word_input = input()
    if word_min == '':
        word_min = word_input
    if word_min > word_max:
        word_max = word_min
    elif word_input > word_max:
        word_max = word_input
    elif word_input < word_min:
        word_min = word_input

magic_number = (ord(word_min[len(word_min)-1]) * ord(word_max[len(word_max)-1])) ** 2

print(magic_number)
