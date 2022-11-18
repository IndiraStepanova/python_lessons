'''
n = int(input())
ls = []
ls_sums = []
for _ in range(n):
    num = int(input())
    ls.append(num)
for i in range(len(ls) - 1):
    nums_sum = ls[i] + (ls[i + 1])
    ls_sums.append(nums_sum)
print(ls_sums)
'''
'''
n = int(input())
ls_sums = []
previous_num = 0
for _ in range(n):
    current_num = int(input())
    ls_sums.append(previous_num + current_num)
    previous_num = current_num
print(ls_sums[1:])
'''
n = int(input())
ls_sums = []
current_num = int(input())
for _ in range(n - 1):
    previous_num = current_num
    current_num = int(input())
    ls_sums.append(previous_num + current_num)
print(ls_sums)