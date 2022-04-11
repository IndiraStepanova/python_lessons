"""Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и 
выводит на стандартный вывод сводную таблицу результатов всех матчей.
За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
Формат ввода следующий:
В первой строке указано целое число n n — количество завершенных игр.
После этого идет n n строк, в которых записаны результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой
Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков"""

game_quantity = int(input())
game_dict = {}
win_dict= {}
draw_dict= {}
defeat_dict= {}
cnt = 0
def win(a, b, some_win_dict, some_defeat_dict):
    if a in win_dict:
        some_win_dict[a] += 1
    else:
        some_win_dict[a] = 1
    if b in some_defeat_dict:
        some_defeat_dict[b] += 1
    else:
        some_defeat_dict[b] = 1
        
def defeat(a, b, some_win_dict, some_defeat_dict):
    if b in some_win_dict:
        some_win_dict[b] += 1
    else:
        some_win_dict[b] = 1
    if a in some_defeat_dict:
        some_defeat_dict[a] += 1
    else:
        some_defeat_dict[a] = 1
        
def draw (a, b, some_draw_dict):
    if a in some_draw_dict:
        some_draw_dict[a] += 1
    else:
        some_draw_dict[a] = 1
    if b in some_draw_dict:
        some_draw_dict[b] += 1
    else:
        some_draw_dict[b] = 1
    
while cnt < game_quantity:
    team1, goal1, team2, goal2 = input().split(';')
    if team1 in game_dict:
        game_dict[team1] += 1
    if team2 in game_dict:
        game_dict[team2] += 1
    if team1 not in game_dict:
        game_dict[team1] = 1
    if team2 not in game_dict:
        game_dict[team2] = 1
    
    if goal1 > goal2:
        win(team1, team2, win_dict, defeat_dict)

    elif goal1 < goal2:
        defeat(team1, team2, win_dict, defeat_dict)

    elif goal1 == goal2:
        draw(team1, team2, draw_dict)
        
    cnt += 1
for key, value in game_dict.items():
    print(key+':', value, sep = "", end = " ")
    print(win_dict.get(key, 0), end = " ")
    print(draw_dict.get(key, 0), end = " ")
    print(defeat_dict.get(key, 0), end = " ")
    print(win_dict.get(key, 0)*3 + draw_dict.get(key, 0)*1, end = "\n")