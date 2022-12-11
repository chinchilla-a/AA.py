def welcome_speech(t):
    print(f'''Добро пожаловать в игру - hangman 2000.
          Ваша задача угадать загаданное слово за несколько попыток,иначе вас ждёт расплата!
          Загаданное слово состоит из {len(t)} букв {t}''')


def start_template(w):
    t = []
    for i in w:
        t.append('_')
    return t


def list_to_string_convert(t):
    """
    input: t - template (list)
    output: s - list convered to string
    """
    s = ''
    return s.join(t)


def get_word(w):
    """
    input: w - list with strings (words)
    output: for now: first element in list as string
            TODO: random string from list
    """
    return w[0]


def user_input():
    """
    output: return built_in input() function
    """
    return input('Введите букву:')


def build_template(t, w, g=''):
    for i in range(len(w)):
        if g == w[i]:
            t[i] = g
    return t


def check_win(g):
    for l in g:
        if l == '_':
            return True
    return False


def check_mistake(w, g):
    flag = False
    for i in w:
        if i == g:
            flag = True
    return flag


def hangman():
    progress = True
    word = ['orange']
    lifes = 3

    word_in_play = get_word(word)
    template = start_template(word_in_play)
    welcome_speech(list_to_string_convert(template))
    while progress:
        user_guess = user_input()
        template = build_template(template, word_in_play, user_guess)
        guessed = list_to_string_convert(template)
        print(f'Результат:{guessed}')
        progress = check_win(guessed)

        if not check_mistake(word_in_play, user_guess):
            print(f'Осталось {lifes} попытки')
            lifes -= 1

        if lifes == -1:
            print("Вы проиграли")
            break
        if not progress:
            print("Вы выиграли")


hangman()
