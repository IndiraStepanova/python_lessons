import time
start_time = time.time()

n = int(input())
for i in range(1, n + 1):
    print(i, end = '')
    for j in range(1, i + 1):
        if i % j == 0:
            print('+', end = '')
    print()


end_time = time.time()
total_time = end_time - start_time
print(total_time)   