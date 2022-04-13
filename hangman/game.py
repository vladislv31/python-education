'''Module that implements class Hangman game'''


import os
import random


# service utils

def clear_screen():
    '''Service method for clear screen'''

    os.system('clear')

def press_key():
    '''Service method for press key'''

    try:
        input('Press any key to continue...')
    except KeyboardInterrupt:
        pass

    clear_screen()

def print_info_msg(msg):
    '''Service method for print info message'''

    print('=========')
    print(msg)
    print('=========')


class Hangman:
    '''Class that implements Hangman game'''

    # pylint: disable=too-many-instance-attributes

    def __init__(self, words_file, previous_words_file, debug=False):
        self.words_file = words_file
        self.previous_words_file = previous_words_file
        self.debug = debug

        self.current_word = None
        self.guess_word = None
        self.to_guess = None

        self.tries = None
        self.used_tries = None

        self.misses = None

        self.is_playing = False

    def run(self):
        '''Run method'''

        while True:
            try:
                print('======== Hangman Game ========')
                print('1. Start the game')
                print('2. Check previous words')
                print('3. Exit')

                choice = int(input("Your choice: "))

                if choice == 1:
                    self.start_game()
                elif choice == 2:
                    self.show_previous_words()
                elif choice == 3:
                    break
                else:
                    print('Unknown choice')

            except ValueError:
                print('Unknown choice')

            except KeyboardInterrupt:
                print('\n')
                break

            press_key()

        print('Goodbye!')

    def start_game(self):
        '''Method that starts game session'''

        clear_screen()

        self.is_playing = True

        if self.debug:
            self.current_word = input('[DEBUG] input current word: ')
        else:
            self.current_word, err, msg = self.get_word()

            if err:
                print(msg)
                return

        self.guess_word = ['_' for _ in range(len(self.current_word))]
        self.to_guess =  list(self.current_word)

        self.tries = 6
        self.used_tries = 0

        self.misses = []

        while self.is_playing:
            if self.debug:
                print(f'[DEBUG] Current word: {self.current_word}\n')

            print(f'Word to guess: {"".join(self.guess_word)}')
            print(f'Tries: {self.tries}')
            print(f'Used tries: {self.used_tries}')
            print(f'Misses: {", ".join(self.misses)}')

            guess = input('Guess: ')
            self.check_guess(guess)

            press_key()

    def check_guess(self, guess):
        '''Method for checking users guess'''

        if guess in self.to_guess:
            self.to_guess.remove(guess)
            self.refresh_guess_word(guess)

            if not self.to_guess:
                self.victory_action()
                self.is_playing = False
        else:
            if guess not in self.misses:
                self.misses.append(guess)
            self.used_tries += 1

            if self.tries == self.used_tries:
                self.loss_action()
                self.is_playing = False

    def refresh_guess_word(self, guessed_letter):
        '''Method for refreshing guessing word'''

        pos = -1

        while True:
            pos = self.current_word.find(guessed_letter, pos + 1)
            if self.guess_word[pos] == '_':
                break

        self.guess_word[pos] = guessed_letter

    def get_word(self):
        '''
        Method to get word from words file with adding it
        to previous words file'''

        words = self.get_words()

        if len(words) < 1:
            return ['', True, 'No words in file...']

        word = random.choice(words)
        words.remove(word)

        self.write_words(words)
        self.add_previous_word(word)

        return [word, False, '']

    def victory_action(self):
        '''Method that calls when user is winner'''

        print_info_msg(f'You are winner! Your word was {self.current_word}')

    def loss_action(self):
        '''Method that calls when user is looser'''

        print_info_msg(f'You lose! Your word was {self.current_word}')

    def show_previous_words(self):
        '''Method that shows previous words'''

        previous_words = self.get_previous_words()

        if len(previous_words) < 1:
            print('Empty...')

        print('\n'.join(previous_words))

    # func for working with files

    def get_words(self):
        '''Get words from file'''

        words = []

        if os.path.exists(self.words_file):
            with open(self.words_file, 'r', encoding='utf-8') as file:
                words = [word.strip('\n') for word in file.readlines()]

        return words

    def get_previous_words(self):
        '''Get previous words from file'''

        previous_words = []

        if os.path.exists(self.previous_words_file):
            with open(self.previous_words_file, 'r', encoding='utf-8') as file:
                previous_words = [word.strip('\n') for word in file.readlines()]

        return previous_words

    def add_previous_word(self, word):
        '''Method that adds previous word to file'''

        with open(self.previous_words_file, 'a', encoding='utf-8') as file:
            file.write(f'{word}\n')

    def write_words(self, words):
        '''Method that writes words back to file'''

        with open(self.words_file, 'w', encoding='utf-8') as file:
            for word in words:
                file.write(f'{word}\n')


if __name__ == '__main__':
    game = Hangman('./words.txt', 'previous_words.txt')
    game.run()
