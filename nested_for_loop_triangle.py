num = int(input())

for i in range(1):
    for j in range(1, (num+1)//2+1):
        print('*' * j)
for k in range(num//2, 0, -1):
    print('*' * k)
    k-=1


def draw_triangle(fill, base):
    for i in range(1):
        for j in range(1, (base + 1) // 2 + 1):
            print(fill * j)
    for k in range(base // 2, 0, -1):
        print(fill * k)
        k -= 1
# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)