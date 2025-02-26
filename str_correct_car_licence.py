car_licence = input()
correct_alpha = 'АВЕКМНОРСТУХ'
flag = "NO"
if len(car_licence[:car_licence.index('_')]) == 6 and \
        car_licence[0] in correct_alpha and \
        car_licence[1:4].isdigit() and \
        car_licence[4] in correct_alpha and \
        car_licence[5] in correct_alpha and \
        car_licence[6] == '_' and \
        car_licence[7:9].isdigit():
    if (len(car_licence[car_licence.index('_')+1:]) == 2 or
        len(car_licence[car_licence.index('_')+1:]) == 3) and \
            car_licence[car_licence.index('_')+1:].isdigit():
        flag = "YES"

print(flag)




