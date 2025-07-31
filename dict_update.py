#https://stepik.org/lesson/446696/step/11?unit=437002

dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}

result = {}
result.update(dict1)
for key, value in dict2.items():
    if key in result:
        result[key] += value
    else:
        result[key] = value
print(result)


###


dict3 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict4 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}

result_2 = {}
result_2.update(dict3)
for key, value in dict4.items():
    result[key] = result_2.get(key, 0) + value
print(result)


