"""
Tests:
    >>> is_palindrome('')
    True
    >>> is_palindrome('abba')
    True
    >>> is_palindrome('ABba')
    True
    >>> is_palindrome('Kobyła ma mały bok')
    True
    >>> is_palindrome('Kobyła ma mały bok.')
    False
    >>> is_palindrome('kociol')
    False
    >>> is_palindrome('kajak')
    True
    >>> is_palindrome('123321')
    True
    >>> is_palindrome('1aa1')
    True
    >>> is_palindrome(12321)
    True
    >>> is_palindrome(12345321)
    False
    >>> is_palindrome(12321.0)
    False
    >>> is_palindrome(123.321)
    True
    >>> is_palindrome(['q', 'd', 'e', 'd', 'q'])
    Traceback (most recent call last):
        ...
    ValueError
    >>> is_palindrome(['q', 'd', 1, (1,2), 1, 'd', 'q'])
    Traceback (most recent call last):
        ...
    ValueError
    >>> is_palindrome(datetime(1111, 11, 11))
    Traceback (most recent call last):
        ...
    ValueError
    >>> is_palindrome('!@#ee#@!')
    True
"""
from datetime import datetime
from typing import Union


def is_palindrome(data: Union[str, int, float]):
    if not isinstance(data, (str, int, float)):
        raise ValueError
    data = str(data).lower().replace(' ', '')
    return data == data[::-1]
