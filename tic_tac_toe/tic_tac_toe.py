'''Module implements class TicTacToe game'''

import logging
import sys

from utils import press_key, clear_screen, input_nes

from exceptions import UknownChoiceException


class TicTacToe: # pylint: disable=too-few-public-methods
    '''TicTacToe game class'''

    # pylint: disable=too-many-instance-attributes

    _win_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                            [0, 3, 6], [1, 4, 7], [2, 5, 8],
                            [0, 4, 8], [2, 4, 6]]

    _area_squares_letters = ['a', 'b', 'c', 'e', 'f', 'g', 'h', 'i', 'j']

    _game_area = None
    _players = None
    _current_player = None
    _winner = None

    _is_playing = False
    _is_session_game = False

    def __init__(self, logs_file):
        self.logs_file = logs_file
        self._setup_logger()

    def _setup_logger(self):
        '''Method setups logger'''

        self.logger = logging.getLogger('TTT Logger')
        self.logger.setLevel(logging.INFO)

        logger_formatter = logging.Formatter(fmt='[%(asctime)s] %(message)s')

        stream_handler = logging.StreamHandler(stream=sys.stdout)
        stream_handler.setFormatter(logger_formatter)

        file_handler = logging.FileHandler(self.logs_file, mode='a')
        file_handler.setFormatter(logger_formatter)

        self.logger.addHandler(stream_handler)
        self.logger.addHandler(file_handler)

    def run(self):
        '''Method runs TicTacToe game'''

        clear_screen()
        is_running = True

        while is_running:
            try:
                print('==== TicTacToe ====')
                print('1. Start the game')
                print('2. Show logs')
                print('3. Clear logs')
                print('4. Exit')

                choice = int(input('Your choice: '))

                if choice == 1:
                    self._start_game_menu()
                elif choice == 2:
                    self._show_logs_menu()
                elif choice == 3:
                    self._clear_logs_menu()
                elif choice == 4:
                    is_running = False
                else:
                    raise UknownChoiceException()
            except (ValueError, UknownChoiceException):
                print('Unknown choice.')
            except KeyboardInterrupt:
                print('\n')
                is_running = False

            press_key()

        print('Good bye!')

    # menu actions

    def _start_game_menu(self):
        '''Method start game'''

        if not self._is_session_game:
            first_player_name = input_nes('Input first player name: ')
            second_player_name = input_nes('Input second player name: ')

            first_player = Player(first_player_name, 'X')
            second_player = Player(second_player_name, 'O')

            self._players = [first_player, second_player]

        self._game_area = [-1 for _ in range(9)]
        round_count = 0

        self._is_playing = True
        while self._is_playing:
            clear_screen()

            round_count += 1
            self._current_player = self._players[(round_count - 1) % 2]

            self._print_game_area()
            player_turn = self._input_turn()
            self._update_game_area_with_turn(player_turn)

            if self._check_winner():
                self._win_game_action()
                continue

            if self._check_if_no_moves():
                self._no_win_game_action()

        choice = input('Do you want to continue playing this session? (y/n): ')
        if choice == 'y':
            self._is_session_game = True
            self._start_game_menu()
        else:
            self._is_session_game = False

    def _show_logs_menu(self):
        '''Method shows logs'''

        print('Logs:')
        with open(self.logs_file, 'r', encoding='utf8') as file:
            logs = file.read()

        if logs:
            print(logs)
        else:
            print('Empty...')

    def _clear_logs_menu(self):
        '''Method clears logs'''

        with open(self.logs_file, 'w', encoding='utf8') as _:
            pass

        print('Logs was successfully cleared.')

    def _win_game_action(self):
        '''Method that called when winner is found'''

        clear_screen()
        self._is_playing = False
        self._winner.increase_score()
        self._print_game_area()
        print(f'{self._winner.get_name()}, you are winner. Congratulations!')
        self.logger.info('%s is winner!', self._winner.get_name())

    def _no_win_game_action(self):
        '''Method that called when friendship is winner'''

        clear_screen()
        self._is_playing = False
        self._print_game_area()
        print('Friendship won.')
        self.logger.info('Friendship is winner!')

    def _update_game_area_with_turn(self, player_turn):
        '''Method updating game area during to player turn'''

        area_box_index = self._area_squares_letters.index(player_turn)
        self._game_area[area_box_index] = self._current_player.get_team()

    def _input_turn(self):
        '''Method allows user to input turn'''

        try:
            turn = input(f'{self._current_player.get_name()}, your turn: ')

            while self._game_area[self._area_squares_letters.index(turn)] != -1:
                turn = input('This square is already occupied, try again: ')
        except ValueError:
            print('Incorrect square choice...')
            return self._input_turn()

        return turn

    def _check_if_no_moves(self):
        '''Method checking for moves availability :)'''

        return len(list(filter(lambda x: x == -1, self._game_area))) == 0

    def _print_players_scores(self):
        '''Method prints players scores as header'''

        print(' vs '.join([str(player) for player in self._players]))

    def _print_game_area(self):
        '''Method prints game area'''

        if self._is_session_game:
            self._print_players_scores()

        print('-------------')

        for idx, square in enumerate(self._game_area):
            if idx % 3 == 0:
                print('|', end='')

            if square == -1:
                print(f' {self._area_squares_letters[idx]} |', end='')
            else:
                print(f' {square} |', end='')

            if idx % 3 == 2:
                print('\n-------------')

    def _check_winner(self):
        '''Method checking if is it a winner'''

        for player in self._players:
            player_team = player.get_team()

            for combination in self._win_combinations:
                score = 0

                for square in combination:
                    if player_team == self._game_area[square]:
                        score += 1

                if score == 3:
                    self._winner = player
                    return True

        return False


class Player:
    '''Class Player'''

    _score = 0

    def __init__(self, name, team):
        self._name = name
        self._team = team

    def get_name(self):
        '''Returns player name'''

        return self._name

    def get_team(self):
        '''Returns player team'''

        return self._team

    def increase_score(self):
        '''Increasing player score'''

        self._score += 1

    def get_score(self):
        '''Returns player score'''

        return self._score

    def __str__(self):
        return f'{self.get_name()} ({self.get_score()} scores)'


if __name__ == '__main__':
    tic_tac_toe = TicTacToe('./ttt.logs')
    tic_tac_toe.run()
