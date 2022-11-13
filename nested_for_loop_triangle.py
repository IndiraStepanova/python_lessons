num = int(input())

for i in range(1):
    for j in range(1, (num+1)//2+1):
        print('*' * j)
for k in range(num//2, 0, -1):
    print('*' * k)
    k-=1