# https://stepik.org/lesson/446696/step/16?unit=437002

my_list = input().split()
result = {}
for symbol in my_list:
    result[symbol]= result.get(symbol, 0) + 1
    if result[symbol] == 1:
        print(symbol, end=' ')
    else:
        print(f'{symbol}_{result[symbol]-1}', end=' ')
   