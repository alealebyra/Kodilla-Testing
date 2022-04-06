from roman_to_integer import roman_to_integer

import pytest


def test_int_input_data_raises_type_error():
    with pytest.raises(TypeError):
        roman_to_integer(13)


def test_not_roman_signs_raises_value_error():
    with pytest.raises(ValueError):
        roman_to_integer('LXDMIXUHWDCS')
