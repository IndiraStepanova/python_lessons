"""
s = input().split()
for i in range(len(s)):
    s[i] = int(s[i])

max_num = max(s)
min_num = min(s)
max_num_index = s.index(max(s))
min_num_index = s.index(min(s))

del s[max_num_index]
s.insert(max_num_index, min_num)

del s[min_num_index]
s.insert(min_num_index, max_num)

for i in range(len(s)):
    s[i] = str(s[i])

s = ' '.join(s)
print(s)
"""

s = input().split()

max_num_index = s.index(max(s, key=int))  # нашли индексы максимальных и минимальных значений;
min_num_index = s.index(min(s, key=int))  # сравнение значений происходит по функции int()

s[max_num_index], s[min_num_index] = s[min_num_index], s[max_num_index]  # обменялись значениями

s = ' '.join(s)
print(s)
