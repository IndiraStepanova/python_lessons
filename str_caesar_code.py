shift, string = int(input()), input()

for char in string:
    decode_char = ord(char) - shift
    if decode_char < 97:
        decode_char += 26
    print(chr(decode_char), end = '')
