#https://stepik.org/lesson/488830/step/14?unit=480066
my_courses = {
    "CS101":	("3004", "Хайнс", "8:00"), 
    "CS102": ("4501", "Альварадо", "9:00"),
    "CS103": ("6755", "Рич", "10:00"),
    "NT110": ("1244", "Берк", "11:00"),
    "CM241": ("1411", "Ли", "13:00")
    }
course_num = input()
audience, teacher, time = my_courses[course_num]


print(f'{course_num}: {audience}, {teacher}, {time}')
