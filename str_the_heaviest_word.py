def sum_word_chars(word):
    chars_sum = 0
    for i in range(len(word)):
        chars_sum += ord(word[i])
    return chars_sum


words = dict()
for _ in range(4):
    w = input()
    words[w] = sum_word_chars(w)


max_key = max(words, key=words.get)


print(max_key)



