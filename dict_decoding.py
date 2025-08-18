#https://stepik.org/lesson/488831/step/7?unit=480067


'''
input_string = input()
n = int(input())
decode_dict, my_code = {}, {}

for _ in range(n):
    letter, cnt = input().split(': ')
    decode_dict[int(cnt)] = letter

for i in input_string:
    my_code[i] = my_code.get(i, 0) + 1

my_dict = {}
for key_code, value_code in my_code.items():
    for key_decode, value_decode in decode_dict.items():
        if value_code == value_decode:
            my_dict[key_code] = key_decode

for i in input_string:
    print(my_dict[i], end='')
'''
input_string = input()
n = int(input())
decode_dict, my_code = {}, {}

for _ in range(n):
    letter, cnt = input().split(': ')
    decode_dict[int(cnt)] = letter

for i in input_string:
    my_code[i] = my_code.get(i, 0) + 1


for i in input_string:
    print(decode_dict[my_code[i]], end='')
    
