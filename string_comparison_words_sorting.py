first_w, second_w, third_w = input(), input(), input()

max_w = max(first_w, second_w, third_w)
min_w = min(first_w, second_w, third_w)
middle_w = ''

if max_w != first_w != min_w:
    middle_w = first_w
elif max_w != second_w != min_w:
    middle_w = second_w
else:
    middle_w = third_w



print(min_w, middle_w, max_w)
