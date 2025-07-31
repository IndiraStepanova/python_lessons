
#https://stepik.org/lesson/446696/step/13?unit=437002

s = "orange strawberry barley gooseberry apple apple apple apple apple apple apple apple apple apple apple apricot barley currant orange melon pomegranate banana banana orange " \
"barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot " \
"currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate " \
"barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot " \
"currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant " \
"orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley".split()

result = {}
for word in s:
    result[word] = result.get(word, 0) + 1

max_dict = {}
for key, value in result.items():
    if value == max(result.values()):
        max_dict[key] = value
print(min(max_dict))
    


