from itertools import cycle
from random import choice

from tictactoe import tic_tac_toe


def play():
    board = ' '*9
    symbol = cycle('XO')

    while ' ' in board:
        field = choice([n for n, s in enumerate(board) if s == ' '])
        board = board[:field] + next(symbol) + board[field+1:]
        print(board)
        winner = tic_tac_toe(board)
        if winner is not None:
            return f'{winner} won!'
    else:
        return 'Tie!'
