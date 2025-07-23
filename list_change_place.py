#https://stepik.org/lesson/415554/step/3?unit=405083

numbers = [int(num) for num in input().split()]    # [1, 2, 3, 4, 5]
for i in range(0, len(numbers)-1, 2):
    numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
print(*numbers)    # 2 1 4 3 5
