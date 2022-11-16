a, b = int(input()), int(input())

for num in range(a, b + 1):
    cnt = 0
    if num == 1:
       continue
    for denominator in range (2, num): # проверяем, что число делится на что-то еще кроме 1 и  самого себя
        if num % denominator == 0:
            cnt += 1
    if cnt == 0:
        print(num)