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

    def get_available_moves(self):
        """Returns available moves"""
        return list(filter(lambda square: isinstance(square, int), self._board))

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

    def reset_move(self, square_idx):
        """Reseting move"""
        self._board[square_idx - 1] = square_idx
        self._last_winner = None

    def check_winner(self, player):
        """Checking player for win"""
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

    def have_winner(self):
        """Checking for having winner"""
        for player in self._players:
            self.check_winner(player)

        return self._last_winner is not None

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


class AIPlayer(Player):
    """AIPlayer"""

    def find_move(self, game_board, player=None): # pylint: disable=too-many-branches
        """Finding successfull move with minimax algorithm"""
        if player is None:
            player = self

        available_moves = game_board.get_available_moves()

        if game_board.have_winner():
            if self is game_board.get_last_winner():
                return {'score': 10}
            return {'score': -10}

        if len(available_moves) == 0:
            return {'score': 0}

        may_moves = []

        for move in available_moves:
            game_board.apply_move(move, player.get_team())

            if isinstance(player, AIPlayer):
                first_player, second_player = game_board.get_players()

                result = self.find_move(game_board, first_player if first_player is not self \
                    else second_player)
                move_score = result['score']
            else:
                result = self.find_move(game_board, self)
                move_score = result['score']

            game_board.reset_move(move)
            may_moves.append({'index': move, 'score': move_score})

        best_move = None

        if player is self:
            best_score = -10000
            for move in may_moves:
                if move['score'] > best_score:
                    best_score = move['score']
                    best_move = move
        else:
            best_score = 10000
            for move in may_moves:
                if move['score'] < best_score:
                    best_score = move['score']
                    best_move = move

        return best_move
