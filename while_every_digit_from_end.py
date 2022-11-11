num = int(input())
while num != 0:
    last_digit = num % 10
    print(last_digit)
    num = num // 10

num = int(input())
while num != 0:
    last_digit = num % 10
    print(last_digit, end='')
    num = num // 10

num = input()
num = int(num[::-1])
print(num)