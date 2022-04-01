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
    >>> is_palindrome('!@#ee#@!')
    True
    >>> is_palindrome(12321)
    Traceback (most recent call last):
        ...
    TypeError
    >>> is_palindrome(12345321)
    Traceback (most recent call last):
        ...
    TypeError
    >>> is_palindrome(12321.0)
    Traceback (most recent call last):
        ...
    TypeError
    >>> is_palindrome(12.3321)
    Traceback (most recent call last):
        ...
    TypeError
    >>> is_palindrome(123.321)
    Traceback (most recent call last):
        ...
    TypeError
    >>> is_palindrome(['q', 'd', 'e', 'd', 'q'])
    Traceback (most recent call last):
        ...
    TypeError
    >>> is_palindrome(['q', 'd', 1, (1,2), 1, 'd', 'q'])
    Traceback (most recent call last):
        ...
    TypeError
    >>> is_palindrome(datetime(1111, 11, 11))
    Traceback (most recent call last):
        ...
    TypeError
"""
from datetime import datetime


def is_palindrome(data: str):
    if not isinstance(data, str):
        raise TypeError
    data = data.lower().replace(' ', '')
    return data == data[::-1]
