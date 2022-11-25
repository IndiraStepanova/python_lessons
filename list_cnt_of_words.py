
"""
string = input().split()
articles_list = ['a', 'an', 'the']
cnt = 0

for word in string:
    for article in articles_list:
        if word.lower() == article.lower():
            cnt += 1
print(f'Общее количество артиклей: {cnt}')
"""
string = input().lower().split()
articles_list = ['a', 'an', 'the']
articles_cnt = 0
for article in articles_list:
    articles_cnt += string.count(article)

print(f'Общее количество артиклей: {articles_cnt}')