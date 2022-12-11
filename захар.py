def welcome_speesh(t):
    print(f'''добро пожаловать в игру виселица
            ваша задача угадать загадонное слово за несколько попыток
            иначе вас ждёт расплата!
            загаданное слово состоит из {len(t)} {t}''')


def start_template(w):
    return len(w) * ['_']


def list_to_string_convert(t):
    s = ''
    return s.join(t)


def get_word(w):
    """
    input: w - list with strings( words)
    output:for now: first element  in  list as string
        TODO:random string from list
    """
    return w[0]


def user_input():
    return input('введите букву:')


def build_template(t, w, g=''):
    for i in range(len(w)):
        if w[i] == g:
            t[i] = g
    return t


def check_win(g):
    for i in g:
        if i == '_':
            return True
    return False


def check_mistake(w, g):
    flag = False
    for i in w:
        if i == g:
            flag = True
    return flag


def game():
    progress = True
    word = ['апельсин']
    lifes = 12

    word_in_play = get_word(word)
    template = start_template(word_in_play)
    welcome_speesh(list_to_string_convert(template))
    while progress:
        user_guess = user_input()
        template = build_template(template, word_in_play, user_guess)
        quessed = list_to_string_convert(template)
        print(f'результат:{quessed}')
        progress = check_win(quessed)
        if not check_mistake(word_in_play, user_guess):
            print(f'осталось {lifes} попыток')
            lifes -= 1
        if lifes == 0:
            print('вы проиграли')
            break
        if not progress:
            print('вы победили')


game()
