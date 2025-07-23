# https://stepik.org/lesson/416753/step/13?unit=406261

symbols = input().split()
cnt = int(input())


def chunked(s, n):
    packadge = []
    while len(s) > 0:
        packadge.append(s[:n])
        del s[:n]
    return packadge


print(chunked(symbols, cnt))
