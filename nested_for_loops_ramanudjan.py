for a in range(1, 34):
    for b in range(a, 34):
        for c in range(a, 34):
            if b != c and a != c:
                for d in range(c, 34):
                    if a != d:
                        if a ** 3 + b ** 3 == c ** 3 + d ** 3:
                            print(f'a = {a}, b = {b}, c = {c}, d = {d}')
                            print(a ** 3 + b ** 3)