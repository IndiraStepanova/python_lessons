'''
# https://stepik.org/lesson/482377/step/13?unit=473680
# Количество совпадающих:
set_1 = set(input().split())
set_2 = set(input().split())
set_1.intersection_update(set_2)
print(len(set_1))
'''


'''
# https://stepik.org/lesson/482377/step/14?unit=473680
# пересечение двух множеств
set_1, set_2 = [[int(i) for i in input().split()] for _ in range(2)]
result = sorted(list(set(set_1).intersection(set_2)))
print(*result)
'''

'''
# https://stepik.org/lesson/482377/step/15?unit=473680
# разность
set_1, set_2 = [[int(i) for i in input().split()] for _ in range(2)]
result = sorted(list(set(set_1).difference(set_2)))
print(*result)
'''

#https://stepik.org/lesson/482377/step/16?unit=473680
#пересечение нескольких множеств
'''n = int(input())
first_str = set(input())
for _ in range(n-1):
    current_str = set(input())
    first_str &= current_str
print(*sorted(first_str))

n = int(input())
my_set = set()
input_nums = sorted([input() for i in range(n)], key=int, reverse=True)
output_set = sorted(list(set(input_nums.pop()).intersection(*input_nums)), key=int)
print(*output_set)
'''
# https://stepik.org/lesson/483114/step/8?unit=474427
# пересекаются ли множества?
set_1, set_2, set_3 = [set([int(i) for i in input().split()]) for _ in range(3)]

# множество чисел, которое встречается в 1 и 2 мн-ве, но отсутствует в 3
print(*sorted(list((set_1 & set_2) - set_3), key=int, reverse=True))

# множество чисел, которое встречается не более, чем в двух множествах
result_1 = (set_1 | set_2 | set_3) - (set_1 & set_2 & set_3)
print(*sorted(list(result_1)))

# множество чисел, которое встречается не более, чем в двух множествах
result_2 = (set_1 | set_2 | set_3) - (set_1 | set_2)
print(*sorted(list(result_2), key=int, reverse=True))

#множество чисел, которые не встречаются ни в одном мн-ве
set_4 = set(range(11))
result_3 = set_4 - (set_1 | set_2 | set_3)
print(*sorted(list(result_3)))

