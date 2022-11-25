keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
new_keywords = [words[1:] for words in keywords]  # новый список, содержащий строки исходного списка с удаленным первым символом
print(new_keywords)

lengths = [len(words) for words in keywords]  # новый список, содержащий длины строк исходного списка.
print(lengths)

new_keywords = [words for words in keywords if len(words) >= 5]  # новый список, содержащий только слова длиной не менее пяти символов (включительно).
print(new_keywords)

palindromes = [nums for nums in range(100, 1001) if str(nums) == str(nums)[::-1]]
palindromes1 = [nums for nums in range(100, 1001) if nums % 10 == nums // 100]
print(palindromes)
print(palindromes1)