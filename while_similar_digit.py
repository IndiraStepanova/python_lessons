import time
start_time = time.time()
num = input()
output = "YES"
max_digit= max(num)
min_digit = min(num)
if max_digit != min_digit:
    output = "NO"
print(output)
end_time = time.time()
total_time = end_time - start_time
print(total_time)


'''import time
start_time = time.time()
num = int(input())
output = "YES"
m = num % 10
while num != 0 and output == 'YES':
    if m != num % 10:
        output = "NO"
    num //= 10
print(output)
end_time = time.time()
total_time = end_time - start_time
print(total_time)'''
    



