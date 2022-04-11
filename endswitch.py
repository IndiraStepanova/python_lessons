x = int(input())
if 0 <= x <= 1000:
    if x % 10 == 1 and x % 100 != 11:
        print(x, 'программист')
    elif x % 10 in (2, 3, 4) and x % 100 not in (12, 13, 14):    
    #elif (x % 10 == 2 or x % 10 == 3 or x % 10 == 4) and x % 100 != 12 and x % 100 != 13 and x % 100 != 14:
        print(x, 'программиста')
    else:   
        print(x, 'программистов')
else:
    print('Введите число от 0 до 1000')