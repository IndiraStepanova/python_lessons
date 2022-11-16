'''
s = input()
output = 'YES'
if s != s[::-1]:
    output = 'NO'
print(output)
'''
s = input()
output = 'YES'
start = 0
end = len(s) - 1
while start < end:
    if s[start] != s[end]:
        output = 'NO'
        break
    start += 1
    end -= 1
print(output)
    