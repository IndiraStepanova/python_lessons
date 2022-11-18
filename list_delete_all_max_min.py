n = int(input())
ls = []

for _ in range(n):
    ls.append(int(input()))

max_n = max(ls)
min_n = min(ls)

for i in range(len(ls)):
    if min_n in ls:
        del ls[ls.index(min_n)]
        # ИЛИ ls.remove(min_n)
    if max_n in ls:
        del ls[ls.index(max_n)]
        # ИЛИ ls.remove(max_n)

print(ls)

