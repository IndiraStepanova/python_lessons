# S=p(p−a)(p−b)(p−c)**0.5 формула Герона; вычисление площади треугольника
# pow(x, y) где x возводится в степень y

a = int(input())
b = int(input())
c = int(input())
p = (a+b+c)/2
S = pow((p*(p-a)*(p-b)*(p-c)), 0.5)
#S_1 = (p*(p-a)*(p-b)*(p-c))**0.5
print(S)
#print(S_1)




