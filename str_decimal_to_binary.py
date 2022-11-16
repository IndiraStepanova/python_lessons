'''
s = int(input())
print(format(int(s), 'b'))
'''
s = int(input())
bin_s = ''
while s // 2 != 0:
    bin_s = bin_s + str(s % 2)
    s //=2
bin_s = bin_s + str(s % 2)
bin_s = bin_s[::-1]
print(bin_s)