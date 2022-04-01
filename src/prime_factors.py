"""
Tests:
    >>> prime_factors(12)
    [2, 2, 3]
    >>> prime_factors(2347)
    [2347]
    >>> prime_factors(3958159172)
    [2, 2, 11, 2347, 38329]
    >>> prime_factors(0)
    Traceback (most recent call last):
        ...
    ValueError
    >>> prime_factors(1)
    Traceback (most recent call last):
        ...
    ValueError
    >>> prime_factors(-18)
    Traceback (most recent call last):
        ...
    ValueError
    >>> prime_factors('Kodilla')
    Traceback (most recent call last):
        ...
    TypeError
    >>> prime_factors(22.22)
    Traceback (most recent call last):
        ...
    TypeError
"""
THE_LOWEST_FACTOR: int = 2


def prime_factors(number: int) -> list:
    if not isinstance(number, int):
        raise TypeError
    if number < THE_LOWEST_FACTOR:
        raise ValueError

    factor: int = THE_LOWEST_FACTOR
    prime_factors_list: list = []

    while factor <= number:
        if number % factor == 0:
            number /= factor
            prime_factors_list.append(factor)
        else:
            factor += 1

    return prime_factors_list


