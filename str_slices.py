s = '01234567891011121314151617'
#1
print(len(s)) # общее количество символов в строке;
print(s * 3) # исходную строку повторенную 3 раза;
print(s[0]) # первый символ строки;
print(s[0:3]) # первые три символа строки;
print(s[-3:]) # последние три символа строки;
print(s[::-1]) # строку в обратном порядке;
print(s[1:-1]) # строку с удаленным первым и последним символом.
#2
print(s[2]) # третий символ этой строки;
print(s[-2]) # предпоследний символ этой строки;
print(s[:5]) # первые пять символов этой строки;
print(s[:-2]) # всю строку, кроме последних двух символов;
print(s[::2]) # все символы с четными индексами;
print(s[1::2]) # все символы с нечетными индексами;
print(s[::-1]) # все символы в обратном порядке;
print(s[::-2]) # все символы строки через один в обратном порядке, начиная с последнего.