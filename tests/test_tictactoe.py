import pytest
from tic_tac_toe.utilities import tic_tac_toe_winner


def test_3x_in_a_row_with_full_board():
    assert tic_tac_toe_winner(
        'xxx'
        'oox'
        'xoo'
    ) == 'X'


def test_3o_in_a_diagonal_with_full_board():
    assert tic_tac_toe_winner(
        'xxo'
        'xox'
        'oox'
    ) == 'O'


def test_3x_in_a_column_with_full_board():
    assert tic_tac_toe_winner('xxooxxoxo') == 'X'


def test_3o_in_a_diagonal():
    assert tic_tac_toe_winner(
        'OX '
        ' O '
        'X O'
    ) == 'O'


def test_3x_in_a_diagonal():
    assert tic_tac_toe_winner(
        'XO '
        ' X '
        'O X'
    ) == 'X'


def test_no_winner_with_full_board():
    assert tic_tac_toe_winner(
        'xxo'
        'oxx'
        'xoo'
    ) is None


def test_no_winner():
    assert tic_tac_toe_winner('oo  x    ') is None


def test_empty_board_raises_value_error():
    with pytest.raises(ValueError):
        tic_tac_toe_winner('')


def test_too_long_board_raises_value_error():
    with pytest.raises(ValueError):
        tic_tac_toe_winner('xxx')


def test_too_long_board_raises_value_error():
    with pytest.raises(ValueError):
        tic_tac_toe_winner('xoxoxoxoxoxoxoxo')


def test_too_much_one_sign_raises_value_error():
    with pytest.raises(ValueError):
        tic_tac_toe_winner('oo   x  o')


def test_too_much_of_one_sign_in_full_board_raises_value_error():
    with pytest.raises(ValueError):
        tic_tac_toe_winner('oooooooxx')


def test_not_allowed_sign_raises_value_error():
    with pytest.raises(ValueError):
        tic_tac_toe_winner('ox t o  x')


def test_invalid_type_of_board_raises_type_error():
    with pytest.raises(TypeError):
        tic_tac_toe_winner(123456789)


def test_more_than_one_winning_configuration_raises_value_error():
    with pytest.raises(ValueError):
        tic_tac_toe_winner('xxxoooxox')
