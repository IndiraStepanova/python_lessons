'''
n = int(input())
ls = []

for _ in range(n):
    string = input()
    ls.append(string)
search_s = input().lower()
for s in ls:
    if search_s in s.lower():
        print(s)

'''

n = int(input())
ls = []
for _ in range(n):
    string = input()
    ls.append(string)

search_ls = []
cnt_search_s = int(input())
for _ in range(cnt_search_s):
    search_s = input()
    search_ls.append(search_s)

for i in ls:
    for j in search_ls:
        if j.lower() not in i.lower():
            break
    else:
        print(i)
