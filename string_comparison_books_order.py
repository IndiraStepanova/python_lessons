n = int(input())
author_and_book = input()
flag = 'YES'


def author_name(s):
    return s[:s.find(' ')]


def book_name(s):
    return s[s.find('«')+1:s.find('»')]


for _ in range(n-1):
    next_author_and_book = input()
    if author_name(author_and_book) < author_name(next_author_and_book):
        flag = 'YES'
        author_and_book = next_author_and_book
    elif book_name(author_and_book) < book_name(next_author_and_book):
        flag = 'YES'
        author_and_book = next_author_and_book
    else:
        flag = 'NO'
        break
print(flag)

