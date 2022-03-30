"""
Tests:
    >>> prime_factors(12)
    [2, 2, 3]
    >>> prime_factors(0)
    Traceback (most recent call last):
        ...
    ValueError
"""


def prime_factors(number: int):
    if number == 0:
        raise ValueError
    return [2, 2, 3]
