s = 1    #1 пирог
a = int(input())     #количество людей в одной группе
b = int(input())     #кол-во людей в другой группе
while s % a != 0 or s % b != 0:
    s += 1     #Увеличиваем кол-во кусочков пирога на 1
print(s)   

'''
a = int(input())
b = int(input())
if   a > b:
      p = a
      while p % b != 0: p += a
elif a < b:
      p = b
      while p % a != 0: p += b
else: p = a
print (p)
'''