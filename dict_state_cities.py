#https://stepik.org/lesson/488831/step/5?unit=480067
n = int(input())
cities_dict = {}
for _ in range(n):
    state, *cities = input().split()
    cities_dict[state] = cities

m = int(input())
for city in range(m):
    city = input()
    for key, values in cities_dict.items():
        if city in values:
            print(key)
