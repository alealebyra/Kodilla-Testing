import pytest
from tictactoe import tic_tac_toe


def test_3x_in_a_row_with_full_board():
    assert tic_tac_toe(
        'xxx'
        'oox'
        'xoo'
    ) == 'x'


def test_3o_in_a_diagonal_with_full_board():
    assert tic_tac_toe(
        'xxo'
        'xox'
        'oox'
    ) == 'o'


def test_3x_in_a_column_with_full_board():
    assert tic_tac_toe('xxooxxoxo') == 'x'


def test_3o_in_a_diagonal():
    assert tic_tac_toe(
        'OX '
        ' O '
        'X O'
    ) == 'o'


def test_3x_in_a_diagonal():
    assert tic_tac_toe(
        'XO '
        ' X '
        'O X'
    ) == 'x'


def test_no_winner_with_full_board():
    assert tic_tac_toe(
        'xxo'
        'oxx'
        'xoo'
    ) is None


def test_no_winner():
    assert tic_tac_toe('oo  x    ') is None


def test_empty_board_raises_value_error():
    with pytest.raises(ValueError):
        tic_tac_toe('')


def test_too_long_board_raises_value_error():
    with pytest.raises(ValueError):
        tic_tac_toe('xxx')


def test_too_long_board_raises_value_error():
    with pytest.raises(ValueError):
        tic_tac_toe('xoxoxoxoxoxoxoxo')


def test_too_much_one_sign_raises_value_error():
    with pytest.raises(ValueError):
        tic_tac_toe('oo   x  o')


def test_too_much_of_one_sign_in_full_board_raises_value_error():
    with pytest.raises(ValueError):
        tic_tac_toe('oooooooxx')


def test_not_allowed_sign_raises_value_error():
    with pytest.raises(ValueError):
        tic_tac_toe('ox t o  x')


def test_invalid_type_of_board_raises_type_error():
    with pytest.raises(TypeError):
        tic_tac_toe(123456789)


def test_more_than_one_winning_configuration_raises_value_error():
    with pytest.raises(ValueError):
        tic_tac_toe('xxxoooxox')
