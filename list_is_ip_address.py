string = input().split('.')
for num in string:
    if int(num) not in range(0, 256):
        print('НЕТ')
        break
else:
    print('ДА')