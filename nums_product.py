# https://stepik.org/lesson/415554/step/6?unit=405083

# входные данные
n = int(input())    # количество элементов в наборе
numbers = [int(input()) for num in range(n)]    # числа набора
m = int(input())    # произведение каких-либо чисел из набора


def is_product(nums, product):
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            if nums[i] * nums[j] == product and i != j:
                return True


if is_product(numbers, m):
    print('ДА')
else:
    print('НЕТ')

