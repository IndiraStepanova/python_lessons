#https://stepik.org/lesson/415554/step/8?unit=405083

result = ['ничья', 'Руслан', 'Тимур', 'Руслан', 'Тимур']
player_move = ['ножницы', 'бумага', 'камень', 'ящерица', 'Спок']
Timur = input()
Ruslan = input()

output_index = player_move.index(Timur) - player_move.index(Ruslan)
output = result[output_index]
print(output)