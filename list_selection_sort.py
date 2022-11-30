a = [78, -32, 5, 39, 58, -5, -63, 7, 6, 9]
n = len(a)

"""
for i in range(n):
    a.insert(n, max(a[:n]))
    a.remove(max(a[:n]))
    n -= 1

print(a)
"""
max_n = max(a)
while n > 0:
    max_n = max(a[:n])
    max_n_index = a.index(max_n)
    n -= 1
    a[n], a[max_n_index] = a[max_n_index], a[n]
print(a)