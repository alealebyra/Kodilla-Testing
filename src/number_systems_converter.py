from re import search
from typing import Union


ROMAN_TO_INT_DICT = {
    'I': 1,
    'IV': 4,
    'V': 5,
    'IX': 9,
    'X': 10,
    'XC': 40,
    'L': 50,
    'LC': 90,
    'C': 100,
    'CD': 400,
    'D': 500,
    'DM': 900,
    'M': 1000,
}

AVAILABLE_NUMBER_SYSTEMS_LIST = ['roman', 'dec']


def number_system_converter(number: Union[str, int], number_system: str):
    roman_signs_regex = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"

    if isinstance(number, str) and number_system == AVAILABLE_NUMBER_SYSTEMS_LIST[0]:
        if len(number) == 0:
            raise ValueError

        if not bool(search(roman_signs_regex, number)):
            raise ValueError
    elif isinstance(number, int) and number_system == AVAILABLE_NUMBER_SYSTEMS_LIST[1]:
        if number <= 0:
            raise ValueError
    else:
        raise ValueError

    if number_system == 'roman':
        total = 0
        for position in range(len(number)):
            first_sign = ROMAN_TO_INT_DICT[number[position]]
            if position + 1 < len(number):
                second_sign = ROMAN_TO_INT_DICT[number[position+1]]
                total += first_sign if first_sign >= second_sign else total - first_sign
            else:
              total = total + first_sign
    else:
        total = ''
        for key in sorted(ROMAN_TO_INT_DICT, key=ROMAN_TO_INT_DICT.get, reverse=True):
            letter_count = int(number/ROMAN_TO_INT_DICT[key])
            print(letter_count)
            total += key * letter_count
            print(total)
            number -= letter_count * ROMAN_TO_INT_DICT[key]
    return total
