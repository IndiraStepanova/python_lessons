#https://stepik.org/lesson/446698/step/12?unit=437004

words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']

result = {key: [ord(letter) for letter in key] for key in words}
print(result)