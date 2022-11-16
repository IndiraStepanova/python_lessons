import time
start_time = time.time()

'''
n = int(input())
digits_sum = 0
while n >= 9:
    while n > 0:
        digit = n % 10
        digits_sum += digit
        n //= 10
    n = digits_sum
    digits_sum = 0
print(n)

'''
n = int(input())
digits_sum = 0
while n > 9:
    n = (n % 10) + (n // 10)
print(n)

end_time = time.time()
total_time = end_time - start_time
print(total_time)          
