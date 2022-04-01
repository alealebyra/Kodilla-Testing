"""
Tests:
    >>> prime_factors(12)
    [2, 2, 3]
    >>> prime_factors(2347)
    [2347]
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
    ValueError
    >>> prime_factors(22.22)
    Traceback (most recent call last):
        ...
    ValueError
"""
THE_LOWEST_FACTOR: int = 2


def prime_factors(number: int) -> list:
    if not isinstance(number, int):
        raise ValueError
    if number < THE_LOWEST_FACTOR:
        raise ValueError

    prime_factors_list: list = []
    _add_flag: bool = True
    factor: int = 2

    while factor <= number:
        if number % factor == 0:
            number /= factor
            prime_factors_list.append(factor)
        else:
            factor += 1

    if len(prime_factors_list) == 0:
        prime_factors_list.append(number)
    return prime_factors_list


