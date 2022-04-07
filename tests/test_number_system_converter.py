from number_systems_converter import number_system_converter

import pytest


def test_int_input_data_raises_type_error():
    with pytest.raises(TypeError):
        number_system_converter(13, 'roman')


def test_not_roman_signs_raises_value_error():
    with pytest.raises(ValueError):
        number_system_converter('LXDMIXUHWDCS', 'roman')


def test_empty_string():
    with pytest.raises(ValueError):
        number_system_converter('', 'roman')


def test_not_correct_roman_number():
    with pytest.raises(ValueError):
        number_system_converter('IIIV', 'roman')


def test_too_big_roman_number():
    with pytest.raises(ValueError):
        number_system_converter('MMMMMDC', 'roman')


def test_roman_number_with_smaller_before_bigger():
    assert number_system_converter('IX', 'roman') == 9


def test_roman_number_with_bigger_before_smaller():
    assert number_system_converter('VI', 'roman') == 6


def test_not_available_number_system():
    with pytest.raises(ValueError):
        number_system_converter('CD', 'bin')


def test_dec_to_roman():
    pass
