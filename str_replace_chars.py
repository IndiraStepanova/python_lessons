#https://stepik.org/lesson/313439/step/11?thread=solutions&unit=295959

sam_response = input()
eng_chars = 'eyopaxcETOPAHXCBM'
rus_chars = 'еуорахсЕТОРАНХСВМ'

chars_replace = dict()
for i in range(len(eng_chars)):
    chars_replace[eng_chars[i]] = rus_chars[i]


def chars_cost(words):
    chars_sum = 0
    for i in range(len(words)):
        chars_sum += ord(words[i])
    return chars_sum * 3


old_cost = chars_cost(sam_response)


for key in chars_replace:
    if key in sam_response:
        sam_response = sam_response.replace(sam_response[sam_response.index(key)], chars_replace.get(key))


new_cost = chars_cost(sam_response)

print(f'''Старая стоимость: {old_cost}🐝
Новая стоимость: {new_cost}🐝''')