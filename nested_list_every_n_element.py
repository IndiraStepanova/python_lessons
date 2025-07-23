new_str = input().split()
n = int(input())
new_list = [new_str[i::n] for i in range(n)]
print(new_list)




