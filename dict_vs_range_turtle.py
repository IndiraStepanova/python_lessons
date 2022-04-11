"""Группа биологов в институте биоинформатики завела себе черепашку.
После дрессировки черепашка научилась понимать и запоминать указания биологов следующего вида:
север 10
запад 20
юг 30
восток 40
где первое слово — это направление, в котором должна двигаться черепашка, а число после слова — 
это положительное расстояние в сантиметрах, которое должна пройти черепашка.

Но команды даются быстро, а черепашка ползёт медленно, и программисты догадались, что можно написать программу,
которая определит, куда в итоге биологи приведут черепашку. Для этого программисты просят вас написать программу, 
которая выведет точку, в которой окажется черепашка после всех команд. 

Для простоты они решили считать, что движение начинается в точке (0, 0), и движение на восток увеличивает первую 
координату, а на север — вторую. Программе подаётся на вход число команд n, которые нужно выполнить черепашке, после 
чего n строк с самими командами. Вывести нужно два числа в одну строку: первую и вторую координату конечной точки черепашки. Все координаты целочисленные."""
#сама мудренность:)
'''cnt = 0
cnt_of_directions = int(input())
dict_of_dir = {'восток': 0, 'запад': 0, 'север': 0, 'юг': 0}
while cnt < cnt_of_directions:
    direction = input().split()
    if direction[0] in dict_of_dir:
        dict_of_dir[direction[0]] += int(direction[1])
    else:
        dict_of_dir[direction[0]] = int(direction[1])
    cnt += 1
    if direction[0] == 'юг':
        dict_of_dir['север'] -= int(direction[1])
    if direction[0] == 'запад':
        dict_of_dir['восток'] -= int(direction[1])
del dict_of_dir['юг']
del dict_of_dir['запад']
for value in dict_of_dir.values():
    print(value, end = ' ')'''

cnt_of_dir = int(input())
east, north = 0, 0
for element in range(cnt_of_dir):
    direction = input().split()
    if direction[0] == 'север':
        north += int(direction[1])
    elif direction[0] == 'юг':
        north -= int(direction[1])
    elif direction[0] == 'восток':
        east += int(direction[1])
    elif direction[0] == 'запад':
        east -= int(direction[1])
print(east, north)
    







    