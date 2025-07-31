#https://stepik.org/lesson/446696/step/15?unit=437002

my_string = input().lower().split()
result = {}
for word in my_string:
    word = word.strip('.,!?:;-')
    result[word] = result.get(word, 0) + 1

min_dict = {}
for key, value in result.items():
    if value == min(result.values()):
        min_dict[key] = value
print(min(min_dict))
