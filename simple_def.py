'''
https://stepik.org/lesson/3372/step/8?auth=login&unit=955
'''

def f(x):
    if x <= -2:
        return 1 - ((x + 2)**2)
    if - 2 < x <= 2:
        return -(x/2)
    if x > 2:
        return ((x - 2)**2) + 1
