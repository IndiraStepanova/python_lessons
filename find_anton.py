#https://stepik.org/lesson/415554/step/10?unit=405083

fridge_cnt = int(input())
fridges = [input() for fridge in range(fridge_cnt)]

anton = 'anton'
output = ''


def find_anton(fridge_name, ltr):
    if ltr in fridge_name:
        return ltr
    else:
        return ''


for fridge in range(fridge_cnt):
    for letter in anton:
        output += find_anton(fridges[fridge], letter)
        current_letter_index = fridges[fridge].find(letter)
        fridges[fridge] = fridges[fridge][current_letter_index:]

    if output == anton:
        print(fridge+1, end=' ')
    output = ''

