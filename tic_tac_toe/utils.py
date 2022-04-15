'''Module with utils for TicTacToe game'''

import os


def clear_screen():
    '''Function clearing console screen'''

    os.system('clear')

def press_key():
    '''Function waiting user to press any key'''

    try:
        input('Press any key to continue...')
    except KeyboardInterrupt:
        pass
    clear_screen()

def input_nes(message):
    '''Input not empty string(nes)'''

    string = input(message)
    while not string:
        print('Empty string detected...')
        string = input(message)

    return string
