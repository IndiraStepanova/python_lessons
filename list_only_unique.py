n = int(input())
ls = []

for _ in range(n):
    string = input()
    if string in ls:
        continue
    ls.append(string)

print(ls)