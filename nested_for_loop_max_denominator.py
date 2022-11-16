a, b = int(input()), int(input())

max_denominators_sum = -1
max_num = -1
for num in range(a, b + 1):
    denominators_sum = 0
    for denominator in range (1, num + 1): 
        if num % denominator == 0:
            denominators_sum += denominator
    if denominators_sum >= max_denominators_sum and denominator > max_num:
        max_denominators_sum = denominators_sum
        max_num = denominator
print(max_num, max_denominators_sum)