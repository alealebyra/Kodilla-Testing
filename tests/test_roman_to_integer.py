from roman_to_integer import roman_to_integer

import pytest


def test_int_input_data_raises_type_error():
    with pytest.raises(TypeError):
        roman_to_integer(13)
