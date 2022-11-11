num = int(input())
is_ordered = 'YES'
last_digit = num % 10
while num != 0 and is_ordered == 'YES':
    pre_last_digit = num % 10
    if last_digit > pre_last_digit:
        is_ordered = 'NO'
    else: 
        last_digit = pre_last_digit
        num //= 10
print(is_ordered)
