# https://stepik.org/lesson/488831/step/1?unit=480067
n = int(input())
my_dict = {}

for _ in range(n):
    word, sense = input().split(': ')
    my_dict[word.lower()] = sense

m = int(input())
for w in range(m):
    w = input().lower()
    print(my_dict.get(w, 'Не найдено'))
    


