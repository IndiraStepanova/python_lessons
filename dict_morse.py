#https://stepik.org/lesson/488830/step/16?unit=480066

letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', 
         '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', 
         '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']

morse_dict = dict(zip(letters, morse))
print(morse_dict)
input_message = input().upper()
for symbol in input_message:
    if symbol in morse_dict:
        print(morse_dict[symbol], end=' ')