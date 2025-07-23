# nested_list_1
# https://stepik.org/lesson/416753/step/8?unit=406261

n = int(input())    # 3
for col in range(n):
    row = [int(i) for i in range(1, n + 1)]
    print(row)
# [1, 2, 3]
# [1, 2, 3]
# [1, 2, 3]

# nested_list_2
# https://stepik.org/lesson/416753/step/9?unit=406261

n = int(input())    # 3
for col in range(1, n+1):
    row = [int(i) for i in range(1, col+1)]
    print(row)
# [1]
# [1, 2]
# [1, 2, 3]
