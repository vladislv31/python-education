"""Module with exceptions for TicTacToe game"""


class UknownChoiceError(Exception):
    """Exception for unknown choice"""


class BadMoveError(Exception):
    """Exception for bad move"""


class EmptyStringError(Exception):
    """Exception for empty string"""
