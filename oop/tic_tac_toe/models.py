"""Module with TicTacToe game models"""

import logging
import sys

from exceptions import BadMoveError

from utils import is_list_items_equals


class GameBoard:
    """Game board"""

    def __init__(self, players, logs_file='tic_tac_toe.logs'):
        self._players = players
        self._logs_file = logs_file

        self._last_winner = None

        self.init_board()
        self._setup_logger()

    def _setup_logger(self):
        """Creates logger"""
        logger_name = 'TicTacToe Logger'
        self._logger = logging.getLogger(logger_name)

        if not self._logger.hasHandlers():
            self._logger.setLevel(logging.INFO)

            logger_formatter = logging.Formatter(fmt='[%(asctime)s] %(message)s')

            stream_handler = logging.StreamHandler(stream=sys.stdout)
            stream_handler.setFormatter(logger_formatter)

            file_handler = logging.FileHandler(self._logs_file, mode='a')
            file_handler.setFormatter(logger_formatter)

            self._logger.addHandler(stream_handler)
            self._logger.addHandler(file_handler)

    def init_board(self):
        """Initing & reseting board"""
        self._board = list(range(1, 10))
        self._last_winner = None

    def get_board(self):
        """Returns board"""
        return self._board

    def get_players(self):
        """Returns players"""
        return self._players

    def get_players_queue(self):
        """Returns players lazy generator"""
        for player in self._players * 4 + [self._players[0]]:
            yield player

    def apply_move(self, square_idx, team):
        """Applying move with checking for its availability"""
        if isinstance(self._board[square_idx - 1], int):
            self._board[square_idx - 1] = team
        else:
            raise BadMoveError('This move is not available.')

    def is_winner(self, player):
        """Checking for winner"""
        player_team = player.get_team()

        # checking columns
        for i in range(3):
            if is_list_items_equals(self._board[i::3], player_team):
                self._last_winner = player
                return True

        # checking rows
        for i in range(0, 7, 3):
            if is_list_items_equals(self._board[i:i+3], player_team):
                self._last_winner = player
                return True

        # checking diagonals
        if is_list_items_equals(self._board[2:8:2], player_team):
            self._last_winner = player
            return True

        if is_list_items_equals(self._board[0:9:4], player_team):
            self._last_winner = player
            return True

        return False

    def log_winner(self):
        """Logs winner or tie"""
        if self._last_winner:
            self._logger.info('%s is winner!', self._last_winner.get_name())
        else:
            self._logger.info('Tie!')

    def get_last_winner(self):
        """Returns last winner"""
        return self._last_winner


class Player:
    """Player model"""

    def __init__(self, name, team):
        self._name = name
        self._team = team
        self._score = 0

    def get_name(self):
        """Returns name"""
        return self._name

    def get_team(self):
        """Returns team"""
        return self._team

    def get_score(self):
        """Returns score"""
        return self._score

    def increase_score(self):
        """Increasing score"""
        self._score += 1

    def __repr__(self):
        return f'{self.get_name()} ({self.get_score()} scores)'
