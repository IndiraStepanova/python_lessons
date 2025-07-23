#https://stepik.org/lesson/415554/step/2?unit=405083


numbers = [int(num) for num in input().split()]
cnt = 0
for i in range(len(numbers)-1):
    current_num = numbers[i]
    next_num = numbers[i+1]
    if current_num < next_num:
        cnt += 1
print(cnt)
