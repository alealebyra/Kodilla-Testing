from re import search


ROMAN_TO_INT_DICT = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

AVAILABLE_NUMBER_SYSTEMS_LIST = ['roman', 'dec']


def number_system_converter(roman_number: str, number_system: str):
    if not isinstance(roman_number, str):
        raise TypeError

    if len(roman_number) == 0:
        raise ValueError

    roman_signs_regex = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
    if not bool(search(roman_signs_regex, roman_number)):
        raise ValueError

    if number_system not in AVAILABLE_NUMBER_SYSTEMS_LIST:
        raise ValueError

    total = 0

    if number_system == 'roman':
        for position in range(len(roman_number)):
            first_sign = ROMAN_TO_INT_DICT[roman_number[position]]
            if position + 1 < len(roman_number):
                second_sign = ROMAN_TO_INT_DICT[roman_number[position+1]]
                total += first_sign if first_sign >= second_sign else total - first_sign
            else:
              total = total + first_sign
    else:
        pass
    return total
