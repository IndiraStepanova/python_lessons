n = int(input())
for i in range(1, n+1):
    comment = input()
    if comment.isspace() or comment == "":
        comment = "COMMENT SHOULD BE DELETED"
    print(f'{i}: {comment}')




