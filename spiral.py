'''Выведите таблицу размером n×n, заполненную числами от 1 до n2 по спирали, выходящей из левого верхнего угла 
и закрученной по часовой стрелке, как показано в примере (здесь n=5)'''

num = int(input())
matrix = [[0]*num for i in range(num)]
coordinate = 1
for lenth in range(len(matrix)):
    for high in range(len(matrix[lenth])):
        while coordinate <= num**2:
            matrix[lenth][high] = coordinate
            if lenth <= high + 1 and lenth + high < num - 1:
                high += 1
            elif lenth < high and lenth + high >= num-1: 
                lenth += 1
            elif lenth >= high and lenth + high > num-1: 
                high -= 1
            else: 
                lenth -= 1
            coordinate += 1
for high in matrix:
    print(*high,sep='\t')
