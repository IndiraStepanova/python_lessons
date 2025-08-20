#https://stepik.org/lesson/446698/step/10?thread=solutions&unit=437004

s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'.split()

result = {int(key): value for key, value in [item.split(':') for item in s]}
print(result)