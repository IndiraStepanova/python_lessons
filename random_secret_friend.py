#https://stepik.org/lesson/356380/step/12?unit=340495

import random

n = int(input())
students = [input() for _ in range(n)]
friends = students.copy()
random.shuffle(friends)
secret_friends = {}
for student in students:
    for friend in friends:
        if friend != student:
            secret_friends[student] = friend
            friends.remove(friend)
            break    #если друг найден, то удаляем его из списка и переходим к следующему студенту
        else:
            continue    #если друг не найден, ищем другого друга

for student in students:
    print(f'{student} - {secret_friends[student]}')



    






