from roman_to_integer import roman_to_integer

import pytest


def test_int_input_data_raises_type_error():
    with pytest.raises(TypeError):
        roman_to_integer(13)


def test_not_roman_signs_raises_value_error():
    with pytest.raises(ValueError):
        roman_to_integer('LXDMIXUHWDCS')


def test_empty_string():
    with pytest.raises(ValueError):
        roman_to_integer('')


def test_not_correct_roman_number():
    with pytest.raises(ValueError):
        roman_to_integer('IIIV')


def test_too_big_roman_number():
    with pytest.raises(ValueError):
        roman_to_integer('MMMMMDC')


def test_roman_number_with_smaller_before_bigger():
    assert roman_to_integer('IX') == 9


def test_roman_number_with_bigger_before_smaller():
    assert roman_to_integer('VI') == 6
