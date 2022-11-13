import time
start_time = time.time()

n = int(input())

'''for i in range(1, n+1):
    for _ in range(i):
        print(i, end='')
    print()'''

for i in range(1, n+1):
    print(str(i) * i)
    

end_time = time.time()
total_time = end_time - start_time
print(total_time)          