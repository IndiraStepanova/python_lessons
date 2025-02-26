china_horoscope = ["Дракон", "Змея", "Лошадь", "Овца", "Обезьяна", "Петух", "Собака", "Свинья", "Крыса", "Бык", "Тигр",
                   "Заяц"]
gregor_year = int(input())


def gregor_year_to_china_horo(gy, ch):
    return ch[((gy - 2000) % 12)]


print(gregor_year_to_china_horo(gregor_year, china_horoscope))
