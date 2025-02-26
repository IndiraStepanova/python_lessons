#https://stepik.org/lesson/334152/step/4?unit=317561

# объявление функции
def draw_triangle():
    h = 8
    lower = 15
    cnt = 1

    for i in range(8):
        print((h-1) * ' ', end='')
        print(cnt * '*')
        h -= 1
        cnt += 2



# основная программа
draw_triangle()  # вызов функции