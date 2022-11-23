# 1
s = input().split()
for i in range(len(s)):
    print(s[i])
# ИЛИ
print('\n'.join(s))
# ИЛИ
print(*s, sep='\n')


# 2
s = input().split('\\')  # C:\Windows\System32\calc.exe
print('\n'.join(s))
