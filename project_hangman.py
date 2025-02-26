import random

word_list = ['человек', 'работа', 'слово', 'место', 'вопрос', 'дом']

guessed_letters = []  # список уже названных букв
guessed_words = []  # список уже названных слов


def get_word():
    w = random.choice(word_list)
    return w.upper()


def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     /|\\
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     /|\\
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     /|\\
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     /|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]


def replace_symbol(user_l, word_compl, word):
    word_compl = list(word_compl)
    for i in range(len(word)):
        if word[i] == user_l:
            word_compl.pop(i)
            word_compl.insert(i, word[i])
    word_compl = ''.join(word_compl)
    return word_compl


def in_guesses(user_l):
    if user_l in guessed_words:
        return True
    elif user_l in guessed_letters:
        return True
    else:
        return False


def play(word):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    tries = 6  # количество попыток
    guessed = False  # сигнальная метка
    print('Давайте играть в угадайку слов!')
    print(display_hangman(tries))
    print(word_completion)
    print()
    while tries > 0 and word_completion != word:
        user_word = input('Введите слово или букву: ').upper()
        # если пользователь ввел слово:
        if user_word.isalpha() and len(user_word) > 1:
            if user_word == word:
                guessed = True
                word_completion = word
                print('Поздравляем, вы угадали слово!')
            elif in_guesses(user_word) is True:
                print(f'Вы уже предлагали слово "{user_word}". Попытка не засчитана')
            else:
                tries -= 1
                guessed_words.append(user_word)
                print(display_hangman(tries))
                print('Вы не угадали загаданное слово')
                print(f'Количество оставшихся попыток: {tries}')
        # если пользователь ввел букву:
        elif user_word.isalpha() and len(user_word) == 1:
            if user_word in word and in_guesses(user_word) is False:
                tries -= 1
                guessed_letters.append(user_word)
                word_completion = replace_symbol(user_word, word_completion, word)
                print('Есть такая буква!')
                print(word_completion)
                print(f'Осталось попыток: {tries}')
                if '_' not in word_completion:
                    guessed = True
            elif in_guesses(user_word) is True:
                print(f'Вы уже предлагали букву {user_word}. Попытка не засчитана')
            else:
                tries -= 1
                guessed_letters.append(user_word)
                print(display_hangman(tries))
                print('Эта буква отсутствует в загаданном слове')
                print(f'Количество оставшихся попыток: {tries}')
        else:
            print('Некорректный ввод. Введите букву или слово целиком')
    if guessed:
        print('Вы выиграили!')
        print(f'Количество использованных попыток: {6-tries}')
    else:
        print('К сожалению, Вы проиграили.')
        print(f'Загаданное слово: {word}')


again = 'Д'
while again.upper() == 'Д':
    word = str(get_word())
    play(word)
    guessed_letters.clear()
    guessed_words.clear()
    again = input('Хотите сыграть еще раз? (д = да) ')
