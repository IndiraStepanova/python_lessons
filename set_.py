# https://stepik.org/lesson/479457/step/14?unit=470432

n,m,k,x,y,z,t,a = int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input())
# прочли только по две книге:
x_2 = n + m - t - x
y_2 = m + k - t - y
z_2 = n + k - t - z
two_books = x_2 + y_2 + z_2
# прочли только по одной книге:
n_1 = k - (z_2 + y_2 + t)
m_1 = m - (x_2 + y_2 + t)
k_1 = n - (x_2 + z_2 + t)
one_book = n_1 + m_1 + k_1
# не прочитали ни одной книги:
no_one = a - two_books - one_book - t
print(one_book, two_books, no_one, sep='\n')



