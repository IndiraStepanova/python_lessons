n = int(input())
quarter_1 = 0
quarter_2 = 0
quarter_3 = 0
quarter_4 = 0
for num in range(n):
    num = input().split()
    x = int(num[0])
    y = int(num[1])
    if y > 0:
        if x > 0:
            quarter_1 += 1
        elif x < 0:
            quarter_2 += 1
    elif y < 0:
        if x < 0:
            quarter_3 += 1
        elif x > 0:
            quarter_4 += 1

print(f'''Первая четверть: {quarter_1}
Вторая четверть: {quarter_2}
Третья четверть: {quarter_3}
Четвертая четверть: {quarter_4}
    ''')