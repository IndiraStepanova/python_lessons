sam_response = input()

chars_sum = 0
for i in range(len(sam_response)):
    chars_sum += ord(sam_response[i])
response_cost = chars_sum * 3

print(f'''Текст сообщения: '{sam_response}'
Стоимость сообщения: {response_cost}🐝''')