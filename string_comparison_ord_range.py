#https://stepik.org/lesson/1402735/step/13?unit=1419697

n = int(input())
for _ in range(n):
    class_num = input()
    if len(class_num) == 2:
        if class_num[0].isdigit() and int(class_num[0]) in range(0, 10):
            if class_num[1].isalpha() and ord(class_num[1]) in range(ord('А'), ord('П')+1):
                print('YES')
            else:
                print('NO')
        else:
                print('NO')
    else:
        print('NO')
'''
n = int(input())
for _ in range(n):
    class_num = input()
    if len(class_num) == 2:
        if class_num[0].isdigit() and int(class_num[0]) in range(0, 10):
            if class_num[1].isalpha() and ord(class_num[1]) in range(ord('А'), ord('П')+1):
                print('YES')
            else:
                print('NO')
        else:
                print('NO')
    else:
        print('NO')
        
'''

n = int(input())
for _ in range(n):
    class_num = input()
    if (
        len(class_num) == 2
        and 0 <= class_num[0] <= 9
        and 'А' <= class_num[1] <= 'П'
    ):
        print('YES')
    else:
        print('NO')


