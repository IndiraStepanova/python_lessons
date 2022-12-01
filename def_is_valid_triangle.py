def is_valid_triangle(side1, side2, side3):
    return side1 < side2 + side3 \
           and side2 < side1 + side3 \
           and side3 < side2 + side1


# считываем данные
s1, s2, s3 = input(), input(), input()

# вызываем функцию
print(is_valid_triangle(s1, s2, s3))
