x = int(input())
if int(000000) <= x <= int(999999):
    if ((x//100000) + (x//10000%10) + (x//1000%10)) == ((x//100%10) + (x//10%10) + (x%10)):
        print('Счастливый')
    else:
        print('Обычный')
elif int(000000) >= x or x >= int(999999):
    print('Введите верное значение')
    
  
'''
a, b, c, d, e, f = input()
n= int(a)+int(b)+int(c)
m= int(d)+int(e)+int(f)
if n==m:
    print('Счастливый')
else:
    print('Обычный')

'''





    
