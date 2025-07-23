#https://stepik.org/lesson/415554/step/3?unit=405083

numbers = [int(num) for num in input().split()]
for i in range(0, len(numbers)-1, 2):
    numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
print(''.join(str(numbers)))
