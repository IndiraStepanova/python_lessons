#https://stepik.org/lesson/415553/step/1?unit=405082

n = int(input())
k = int(input())
men_nums = [num for num in range(1, n + 1)]

while len(men_nums) > 1:
    for i in range(1, k):
        temp = men_nums.pop(0)
        men_nums.append(temp)
    men_nums.pop(0)
print(men_nums[0])



