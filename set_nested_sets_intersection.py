m = int(input())
my_list = list()
my_set = list()
for lists in range(m):
    n = int(input())
    my_set = set()
    for surname in range(n):
        my_set.add(input())
    my_list.append(my_set)
print(*sorted(set.intersection(*my_list)), sep='\n')


