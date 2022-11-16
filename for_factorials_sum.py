'''
num = int(input())
f_sum = 0

for n in range(1, num + 1):
    f_mult = 1
    for m in range (1, n + 1): 
        f_mult *= m
    f_sum += f_mult        
print(f_sum)
    
'''
'''
from math import factorial
num = int(input())
f_sum = 0
for n in range(1, num + 1):
    f_sum += factorial(n)
print(f_sum)
'''
num = int(input())
f_sum = 0
f_mult = 1
for n in range(1, num + 1):
    f_mult *= n
    f_sum += f_mult
print(f_sum)