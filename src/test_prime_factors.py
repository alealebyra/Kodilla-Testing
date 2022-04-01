import pytest
from prime_factors import prime_factors


def test_small_number():
    assert prime_factors(12) == [2, 2, 3]


def test_prime_number():
    assert prime_factors(2347) == [2347]


def test_big_number():
    assert prime_factors(3958159172) == [2, 2, 11, 2347, 38329]


def test_zero_raises_value_error():
    with pytest.raises(ValueError):
        prime_factors(0)


def test_one_raises_value_error():
    with pytest.raises(ValueError):
        prime_factors(1)


def test_negative_number_raises_value_error():
    with pytest.raises(ValueError):
        prime_factors(-18)


def test_string_raises_type_error():
    with pytest.raises(TypeError):
        prime_factors('Kodilla')


def test_float_raises_type_error():
    with pytest.raises(TypeError):
        prime_factors(22.22)
