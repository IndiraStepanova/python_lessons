'''
n = int(input())
ls = []
for _ in range(n):
    string = input()
    ls.append(list(string))
output_index = int(input())
for i in range(len(ls)):
    if len(ls[i]) < output_index:
        continue
    print(ls[i][output_index - 1], end='')
'''

n = int(input())
ls = []
for _ in range(n):
    string = input()
    ls.append(string)
output_index = int(input())    
output_string = ''
for s in ls:
    if len(s) >= output_index:
        output_string += s[output_index - 1]
    
print(output_string)