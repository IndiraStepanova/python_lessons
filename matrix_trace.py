# https://stepik.org/lesson/416754/step/10?unit=406262

n = int(input())
matrix = [input().split() for row in range(n)]
trace = 0
for row in range(n):
    trace += int(matrix[row][row])
print(trace)
