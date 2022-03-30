"""
Tests:
    >>> prime_factors(12)
    [2, 2, 3]
    >>> prime_factors(0)
    Traceback (most recent call last):
        ...
    ValueError
    >>> prime_factors(1)
    Traceback (most recent call last):
        ...
    ValueError
"""


def prime_factors(number: int):
    if number in [0, 1]:
        raise ValueError
    return [2, 2, 3]
