from re import sub


def roman_to_integer(roman_number: str):
    if not isinstance(roman_number, str):
        raise TypeError

    allowed_roman_signs_regex = '[^IVXLCDM]+'
    if roman_number != sub(allowed_roman_signs_regex, '', roman_number):
        raise ValueError
