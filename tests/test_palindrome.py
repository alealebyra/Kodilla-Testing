import pytest

from datetime import datetime
from palindrome import is_palindrome


def test_empty_string():
    assert is_palindrome('')


def test_palindrome_with_small_letters():
    assert is_palindrome('abba')


def test_palindrome_with_big_letters():
    assert is_palindrome('ABba')


def test_full_sentence_palindrome():
    assert is_palindrome('Kobyła ma mały bok')


def test_full_sentence_with_punctuation():
    assert not is_palindrome('Kobyła ma mały bok.')


def test_small_letters():
    assert not is_palindrome('kociol')


def test_small_letters_palindrome_with_odd_number_of_letters():
    assert is_palindrome('kajak')


def test_string_with_numbers():
    assert is_palindrome('123321')


def test_string_with_numbers():
    assert is_palindrome('123321')


def test_string_with_letters_and_numbers():
    assert is_palindrome('1aa1')


def test_string_with_letters_and_special_signs():
    assert is_palindrome('!@#ee#@!')


def test_int_input_data_raises_type_error():
    with pytest.raises(TypeError):
        is_palindrome(12345321)


def test_float_input_data_raises_type_error():
    with pytest.raises(TypeError):
        is_palindrome(12.3321)


def test_list_with_strings_input_data_raises_type_error():
    with pytest.raises(TypeError):
        is_palindrome(['q', 'd', 'e', 'd', 'q'])


def test_list_input_data_raises_type_error():
    with pytest.raises(TypeError):
        is_palindrome(['q', 'd', 1, (1,2), 1, 'd', 'q'])


def test_datetime_input_data_raises_type_error():
    with pytest.raises(TypeError):
        is_palindrome(datetime(1111, 11, 11))

