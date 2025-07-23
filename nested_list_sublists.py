# https://stepik.org/lesson/416753/step/14?unit=406261
symbols = '1 2 3 0'.split()
result = [[]]
for i in range(1, len(symbols) + 1):
    for j in range(len(symbols) - i + 1):
        temp = symbols[j:j+i]
        result.append(temp)
print(result)





