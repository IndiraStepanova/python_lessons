# выводим список чисел от 1 до n
'''
n = int(input()) 
print(list(range(1, n + 1))
'''
# выводим список из n букв алфавита
alpha_range = int(input())
alpha_start = int(97)
alphabet = []

for char in range(alpha_start, alpha_start + alpha_range):
    alphabet += chr(char)
print(alphabet)