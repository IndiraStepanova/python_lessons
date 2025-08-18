#https://stepik.org/lesson/488831/step/6?unit=480067
n = int(input())
contacts = {}
for _ in range(n):
    tel, owner = input().split()
    contacts[owner.lower()] = contacts.get(owner.lower(), []) + [tel]
print(contacts)

m = int(input())
for _ in range(m):
    print(*contacts.get(input().lower(), ['абонент не найден']))


