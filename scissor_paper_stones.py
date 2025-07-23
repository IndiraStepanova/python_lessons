# https://stepik.org/lesson/415554/step/7?unit=405083
# входные данные
result = ['Тимур', 'Руслан', 'ничья']
paper = 'бумага'
scissors = 'ножницы'
move = [input() for _ in range(2)]

if move[0] != move[1]:
    if (paper in move) and (scissors in move):
        choice_index = move.index(max(move))
        print(result[choice_index])
    else:
        choice_index = move.index(min(move))
        print(result[choice_index])
else:
    print(result[2])

'''
moves = ["камень", "ножницы", "бумага"]
outcomes = ["ничья", "Руслан", "Тимур"]

timur_move = input()
ruslan_move = input()

difference = moves.index(timur_move) - moves.index(ruslan_move)
result = outcomes[difference]

print(result)
'''



