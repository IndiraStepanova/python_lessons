n = input().split()
packadge = [[n.pop(0)]]
for element in n:
    if element in packadge[-1]:
        packadge[-1].append(element)
    else:
        packadge.append([element])
print(packadge)
