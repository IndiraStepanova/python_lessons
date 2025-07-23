#https://stepik.org/lesson/445791/step/15?unit=436052

n = int(input())
students = [input().split(': ') for _ in range(n)]
set_correct = set()
correct_cnt = 0
cnt = 0
result = 'Correct'
for student in students:
    if student[1] == result:
        set_correct.add(student[0])
        correct_cnt += 1

if n > 0:
    cnt = int((correct_cnt / n) * 100 + 0.5)

print(f'''Верно решили {len(set_correct)} учащихся
Из всех попыток {cnt}% верных
''' if cnt > 0 else 'Вы можете стать первым, кто решит эту задачу')