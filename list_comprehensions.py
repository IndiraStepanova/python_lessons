keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
new_keywords = [words[1:] for words in keywords]  # новый список, содержащий строки исходного списка с удаленным первым символом
print(new_keywords)

lengths = [len(words) for words in keywords]  # новый список, содержащий длины строк исходного списка.
print(lengths)

new_keywords = [words for words in keywords if len(words) >= 5]  # новый список, содержащий только слова длиной не менее пяти символов (включительно).
print(new_keywords)

# список всех чисел палиндромов от 100 до 1000:
palindromes = [nums for nums in range(100, 1001) if str(nums) == str(nums)[::-1]]
print(palindromes)
# ИЛИ:
palindromes1 = [nums for nums in range(100, 1001) if nums % 10 == nums // 100]
print(palindromes1)

# квадраты чисел от 1 до n
n = int(input())
squares = [print(pow(num, 2)) for num in range(1, n + 1)]

# кубы чисел
cubes = [print(pow(int(num), 3), end=' ') for num in input().split()]

# слова введенной строки в столбик:
n = input().split()
line_by_line = [print(word) for word in n]
#ИЛИ:
line_by_line = print('\n'.join(n))

# вывести все цифровые символы введенной строки (н-р, "Число Pi примерно равно 3.1415")
only_digits = [print(symbol, end='') for symbol in input() if symbol.isdigit()]

# вывести квадраты четных чисел. Квадраты не оканчиваются на цифру 4
even_squares = [print(pow(int(num), 2), end=' ') for num in input().split() if int(num) % 2 == 0 and pow(int(num), 2) % 10 != 4]

# вывести список четных чисел от 2 до n
print([i for i in range(2, int(input()) + 1, 2)])

# длина самого длинного слова из строки
print(max([len(i) for i in input().split()]))