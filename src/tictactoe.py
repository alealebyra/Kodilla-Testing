"""
Tests:
    >>> tic_tac_toe('xxxooxxoo')
    'x'
    >>> tic_tac_toe('xxoxoxoox')
    'o'
    >>> tic_tac_toe('xxooxxoxo')
    'x'
    >>> tic_tac_toe('OX  O X O')
    'o'
    >>> tic_tac_toe('XO  X O X')
    'x'
    >>> tic_tac_toe('xxooxxxoo')
    >>> tic_tac_toe('oo  x    ')
    >>> tic_tac_toe('')
    Traceback (most recent call last):
        ...
    ValueError: Board length should be 9, got 0!
    >>> tic_tac_toe('xxx')
    Traceback (most recent call last):
        ...
    ValueError: Board length should be 9, got 3!
    >>> tic_tac_toe('oo   x  o')
    Traceback (most recent call last):
        ...
    ValueError: One of the players make too much moves! Player x moves: 1. Player o moves: 3
    >>> tic_tac_toe('oooooooxx')
    Traceback (most recent call last):
        ...
    ValueError: One of the players make too much moves! Player x moves: 2. Player o moves: 7
    >>> tic_tac_toe("xoxoxoxoxoxoxoxo")
    Traceback (most recent call last):
        ...
    ValueError: Board length should be 9, got 16!
    >>> tic_tac_toe('ox t o  x')
    Traceback (most recent call last):
        ...
    ValueError: The allowed signs in board are 'x', 'o' and ' '!
    >>> tic_tac_toe(123456789)
    Traceback (most recent call last):
        ...
    TypeError: The argument board have to be str, got <class 'int'>!
    >>> tic_tac_toe('xxxoooxox')
    Traceback (most recent call last):
        ...
    ValueError: The given table is impossible to reach. There is more than 1 winning configuration
"""
from re import sub
from typing import Optional

BOARD_LEN = 9


def tic_tac_toe(board: str) -> Optional[str]:
    if type(board) != str:
        raise TypeError(f"The argument board have to be str, got {type(board)}!")
    if len(board) != BOARD_LEN:
        raise ValueError(f"Board length should be {BOARD_LEN}, got {len(board)}!")

    board = board.lower()
    if abs(board.count('x') - board.count('o')) > 1:
        raise ValueError(
            "One of the players make too much moves! "
            f"Player x moves: {board.count('x')}. Player o moves: {board.count('o')}"
        )
    allowed_signs_regex = '[^xo ]+'
    if board != sub(allowed_signs_regex, '', board):
        raise ValueError("The allowed signs in board are 'x', 'o' and ' '!")

    winners = ''
    for position in range(3):
        # columns check
        if board[position] in 'xo':
            if board[position] == board[position + 3] == board[position + 6]:
                winners += board[position]

        # rows check
        if board[position * 3] in 'xo':
            if board[position * 3] == board[position * 3 + 1] == board[position * 3 + 2]:
                winners += board[position * 3]

    # diagonals check
    if board[4] in 'xo':
        if board[0] == board[4] == board[8]:
            winners += board[4]
        if board[2] == board[4] == board[6]:
            winners += board[4]

    if len(winners) > 1:
        raise ValueError("The given table is impossible to reach. There is more than 1 winning configuration")
    elif len(winners) == 1:
        return winners
    else:
        return None
