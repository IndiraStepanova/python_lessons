#shift - направление сдвига
shift, string = int(input()), input()

for char in string:
    decode_char = ord(char) - shift
    if decode_char < ord('А'):
        decode_char += 32
    print(chr(decode_char), end = '')
