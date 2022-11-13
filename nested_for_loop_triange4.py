import time
start_time = time.time()

n = int(input())

for row in range(1, n + 1):
    for col_1 in range(1, row+1):
        print(col_1, end='')
    for col_2 in range(row-1, 0, -1):
        print(col_2, end='')
    print()

end_time = time.time()
total_time = end_time - start_time
print(total_time)          