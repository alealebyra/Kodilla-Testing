from re import search


def roman_to_integer(roman_number: str):
    if not isinstance(roman_number, str):
        raise TypeError

    if len(roman_number) == 0:
        raise ValueError

    roman_signs_regex = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
    if not bool(search(roman_signs_regex, roman_number)):
        raise ValueError
