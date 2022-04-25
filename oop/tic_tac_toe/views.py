"""TicTacToe views"""

from abc import ABC, abstractmethod

from utils import clear_screen

from exceptions import EmptyStringError


class View(ABC):
    """Abstract View Class"""

    # pylint: disable=missing-function-docstring

    @abstractmethod
    def show_menu(self):
        pass

    @abstractmethod
    def show_game_board(self, game_board):
        pass

    @abstractmethod
    def input_string_field(self, field_name):
        pass

    @abstractmethod
    def input_player_move(self, player):
        pass

    @abstractmethod
    def ask_for_continue(self):
        pass

    @abstractmethod
    def show_scores(self, game_board):
        pass

    @abstractmethod
    def show_winner(self, player):
        pass

    @abstractmethod
    def show_tie(self):
        pass

    @abstractmethod
    def show_error(self, msg):
        pass

    @abstractmethod
    def show_logs(self, logs):
        pass

    @abstractmethod
    def clear_logs(self):
        pass

    @abstractmethod
    def clear_terminal(self):
        pass


class UnixTerminalView(View):
    """View for terminals unix systems"""

    def show_menu(self):
        print('==== TicTacToe ====')
        print('1. Start the game')
        print('2. Show logs')
        print('3. Clear logs')
        print('4. Exit')

        choice = int(input('Your choice: '))
        return choice

    def show_game_board(self, game_board):
        """Prints game board"""
        print('-------------')
        for idx, square in enumerate(game_board.get_board()):
            if idx % 3 == 0:
                print('|', end='')
            print(f' {square} |', end='')
            if idx % 3 == 2:
                print('\n-------------')

    def input_string_field(self, field_name):
        """Inputing filed and returning it"""
        try:
            result = input(f'Please, input {field_name}: ')
            if len(result) < 1:
                raise EmptyStringError('Value length should be more than zero.')
            return result
        except EmptyStringError as error:
            self.show_error(error)
            return self.input_string_field(field_name)

    def input_player_move(self, player):
        """Inputing player move with checking for error and returning it"""
        try:
            result = int(input(f'{player.get_name()}, you are playing ' +
                f'for {player.get_team()}s, your next move: '))
            return result
        except ValueError:
            print('You should input an integer.')
            return self.input_player_move(player)

    def ask_for_continue(self):
        """Asking for continue and returning result"""
        ask = input('Do you want to continue playing this session? (y/n): ')

        return ask == 'y'

    def show_scores(self, game_board):
        """Prints scores"""
        players = game_board.get_players()
        print(' vs '.join([str(player) for player in players]))

    def show_winner(self, player):
        """Prints winner"""
        print(f'{player.get_name()} is winner!')

    def show_tie(self):
        """Prints tie"""
        print('Tie! We have no winners!')

    def show_error(self, msg):
        """Prints error"""
        print(f'[Error] {msg}')

    def show_logs(self, logs):
        """Prints logs"""
        print('Logs:')
        if logs:
            print(logs)
        else:
            print('Empty for now...')

    def clear_logs(self):
        """Print message for clear logs"""
        print('Logs was successfully cleared.')

    def clear_terminal(self):
        """Clears terminal"""
        clear_screen()
