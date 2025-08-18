#https://stepik.org/lesson/488831/step/2?unit=480067
'''
first_word = input()
second_word = input()
first_dict = {}
second_dict = {}
for letter in first_word:
    first_dict[letter] = first_dict.get(letter,0) + 1

for letter in second_word:
    second_dict[letter] = second_dict.get(letter,0) + 1

print('YES' if first_dict == second_dict else 'NO')

'''

#https://stepik.org/lesson/488831/step/3?unit=480067
first_s = [c for c in input().lower() if c.isalpha()]
sec_s  = [c for c in input().lower() if c.isalpha()]
f_dict = {}
s_dict = {}

for letter in first_s:
    f_dict[letter] = f_dict.get(letter, 0) + 1

for letter in sec_s:
    s_dict[letter] = s_dict.get(letter, 0) + 1  

print('YES' if f_dict == s_dict else 'NO')