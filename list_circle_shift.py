#https://stepik.org/lesson/415554/step/4?unit=405083

numbers = [int(num) for num in input().split()]   # [1, 2, 3, 4, 5]
'''
numbers.insert(0, numbers[-1])
numbers.pop()
print(*numbers)
'''
for i in range(len(numbers)-1):
    numbers[i], numbers[-1] = numbers[-1], numbers[i]
print(*numbers)
