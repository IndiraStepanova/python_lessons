#https://stepik.org/lesson/360941/step/12?unit=345464

from decimal import Decimal
num = Decimal(input())
nums_digits = num.as_tuple().digits
print(max(nums_digits) + min(nums_digits) * (abs(num) >=1 ))    # abs(num) >= 1 дает 1 или 0, далее в соотв. с очередностью выполняются действия

        
output = num.exp() + num.ln() + num.log10() + num.sqrt()
print(output)