#https://stepik.org/lesson/446698/step/11?unit=437004

numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]
'''
result = {}
for num in numbers:
    for divider in range(1, num+1):
        if num % divider == 0:
            result.setdefault(num, []).append(divider) 
'''

result = {num: [value for value in range(1, num + 1) if num % value == 0] for num in numbers}
print(result)