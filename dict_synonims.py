#https://stepik.org/lesson/488831/step/4?unit=480067
n = int(input())
my_dict = {}

for _ in range(n):
    word, synonim = input().split()
    my_dict[word] = synonim
    my_dict[synonim] = word

w = input()
if w in my_dict:
    print(my_dict[w])
