"""TicTacToe Controllers"""

from os.path import exists as file_exists

from models import GameBoard, Player

import config

from exceptions import BadMoveError, UknownChoiceError

from utils import press_key, clear_screen


class Controller:
    """Tic Tac Toe Controller"""

    def __init__(self, view):
        self.view = view

    def index(self):
        """Index controller"""
        clear_screen()
        is_running = True

        while is_running:
            try:
                choice = self.view.show_menu()

                if choice == 1:
                    self.start_game()
                elif choice == 2:
                    self.show_logs()
                elif choice == 3:
                    self.clear_logs()
                elif choice == 4:
                    is_running = False
                else:
                    raise UknownChoiceError()
            except (ValueError, UknownChoiceError):
                self.view.show_error('Unknown choice.')
            except KeyboardInterrupt:
                is_running = False

            press_key()

    def start_game(self):
        """Starts game with tracking moves and session functionality"""
        first_player_name = self.view.input_string_field('first player name')
        second_player_name = self.view.input_string_field('second player name')

        first_player = Player(first_player_name, 'X')
        second_player = Player(second_player_name, 'O')

        game_board = GameBoard([first_player, second_player], logs_file=config.LOGS_FILE)

        is_session = False
        while True:
            is_winner = False
            for player in game_board.get_players_queue():
                self.view.clear_terminal()
                if is_session:
                    self.view.show_scores(game_board)
                self.view.show_game_board(game_board)

                self._input_move_with_tracking_errors(player, game_board)

                # check win
                if game_board.is_winner(player):
                    is_winner = True
                    player.increase_score()
                    break

            self.view.clear_terminal()
            if is_session:
                self.view.show_scores(game_board)
            self.view.show_game_board(game_board)

            game_board.log_winner()

            if is_winner:
                self.view.show_winner(game_board.get_last_winner())
            else:
                self.view.show_tie()

            if self.view.ask_for_continue():
                is_session = True
                game_board.init_board()
                continue

            break

    def show_logs(self):
        """Gets logs and sends it to self.view"""
        logs = None
        if file_exists(config.LOGS_FILE):
            with open(config.LOGS_FILE, 'r', encoding='utf8') as file:
                logs = file.read()

        self.view.clear_terminal()
        self.view.show_logs(logs)

    def clear_logs(self):
        """Removes logs"""
        with open(config.LOGS_FILE, 'w', encoding='utf8') as _:
            pass

        self.view.clear_terminal()
        self.view.clear_logs()

    def _input_move_with_tracking_errors(self, player, game_board):
        while True:
            try:
                move = self.view.input_player_move(player)
                game_board.apply_move(int(move), player.get_team())
                break
            except BadMoveError as error:
                self.view.show_error(error)
