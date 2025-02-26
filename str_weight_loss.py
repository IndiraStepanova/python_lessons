from math import floor, ceil

weight_loss_day = int(input())
current_weight = float(input())
target_for_weight_loss = round(100 - (weight_loss_day * (100 - 88) / 60), 1)

output = f'#{weight_loss_day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {current_weight} кг, ЦЕЛЬ по ВЕСУ = {target_for_weight_loss} кг'

message = "Все идет по плану"
if current_weight > target_for_weight_loss:
    message = "Что-то пошло не так"

print(f'''{message}
{output}''')
