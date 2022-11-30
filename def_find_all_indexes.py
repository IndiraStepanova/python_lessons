# объявление функции
def find_all(target, symbol):
    return [i for i in range(len(target)) if symbol in target[i]]



# считываем данные
s = input()
char = input()

# вызываем функцию
print(find_all(s, char))