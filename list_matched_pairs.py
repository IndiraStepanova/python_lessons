#https://stepik.org/lesson/324755/step/16?unit=307931

s = input().split()
cnt = 0

for i in range(len(s)):
    for j in s[i+1:]:
        if s[i] == j:
            cnt += 1
print(cnt)





