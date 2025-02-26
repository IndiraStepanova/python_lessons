#https://stepik.org/lesson/349851/step/10?unit=333706


num = input()
if num.isdigit():
    bin_sys = bin(int(num))[2:]
    oct_sys = oct(int(num))[2:]
    hex_sys = hex(int(num))[2:].upper()
    print(f'''{bin_sys}
{oct_sys}
{hex_sys}''')



