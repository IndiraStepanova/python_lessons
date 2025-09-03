import random
import string
'''
n = int(input())    # количество попыток
for _ in range(n):
    print(random.randint(1, 6))
'''
'''
length = int(input())    # длина пароля
symbols_ASCII = [i for i in range(65, 91)] + [i for i in range(97, 123)]
for _ in range(length):
    print(chr(random.choice(symbols_ASCII)), end='')
'''
'''
nums_set = set()
while len(nums_set) != 7:
    nums_set.add(random.randint(1, 49))
print(*sorted(nums_set))
'''


def generate_ip():
    new_ip = [str(random.randrange(256)) for _ in range(4)]
    return '.'.join(new_ip)

def generate_index():
    first_letter_part = ''.join(random.sample(string.ascii_uppercase, 2))
    number_part = '_'.join([str(random.randrange(100)) for _ in range(2)])
    sec_letter_part = ''.join(random.sample(string.ascii_uppercase, 2))
    return f'{first_letter_part}{number_part}{sec_letter_part}'

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

for nested_m in matrix:
    random.shuffle(nested_m)


'''
lottery_set = set()
while len(lottery_set) != 100:
    new_str = random.randint(1000000, 9999999)
    lottery_set.add(str(new_str))
#print(*lottery_set, sep='\n')
'''

word = list(input())
random.shuffle(word)
print(''.join(word))
