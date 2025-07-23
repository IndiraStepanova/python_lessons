# https://stepik.org/lesson/416753/step/12?unit=406261

n = input().split()
packadge = [[n.pop(0)]]
for element in n:
    if element in packadge[-1]:
        packadge[-1].append(element)
    else:
        packadge.append([element])
print(packadge)
