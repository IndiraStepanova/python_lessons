import time
start_time = time.time()
price = int(input())
cnt = 0
coin25 = 25
coin10 = 10
coin5 = 5
coin1 = 1
while price >= coin25:
    price -= coin25
    cnt += 1
while coin25 > price >= coin10:
    price -= coin10
    cnt += 1
while coin10 > price >= coin5:
    price -= 5
    cnt += 1
while coin5 > price >= coin1:
    price -= 1
    cnt += 1 
print(cnt)
end_time = time.time()
total_time = end_time - start_time
print(total_time)