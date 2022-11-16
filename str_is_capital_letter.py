'''
s = input()
output = 'YES'
if s != s.title():
    output = 'NO'
print(output)

name, surname = input().split()
output = 'NO'
if name[0] == name[0].upper() and surname[0] == surname[0].upper():
    output = 'YES'
print(output)
'''
s = input()
space = s.find(' ')
name, surname = s[:space], s[space + 1:]
output = 'NO'
if name[0] == name[0].upper() and surname[0] == surname[0].upper():
    output = 'YES'
print(output)