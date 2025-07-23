from math import floor, ceil, trunc

n = int(input())

def pascal(n):
    prev_result = 1
    pascal_row = [1]
    numerator = n
    for denominator in range(1, n+1):
        prev_result *= numerator/denominator
        pascal_row.append(int(round(prev_result)))
        numerator -= 1
    return pascal_row

print(pascal(n))
