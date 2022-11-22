n = int(input())
neg = []
zeros = []
pos = []

for _ in range(n):
    num = int(input())
    if num < 0:
        neg.append(num)
    elif num > 0:
        pos.append(num)
    else:
        zeros.append(num)

if len(neg) > 0:
    print(*neg, sep='\n')
if len(zeros) > 0:
    print(*zeros, sep='\n')
if len(pos) > 0:
    print(*pos, sep='\n')

