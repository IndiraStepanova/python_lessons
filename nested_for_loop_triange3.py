import time
start_time = time.time()

n = int(input())
num = 0
for row in range(1, n + 1):
    for col in range(1, row + 1):
        num += 1
        print(num, end=' ')
    print()


end_time = time.time()
total_time = end_time - start_time
print(total_time)          