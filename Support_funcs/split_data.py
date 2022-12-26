from Support_funcs.phone_validator import *


def split_data(data: str) -> tuple:
    normalize_data = data.strip()
    name = normalize_data.split(' ')[0].title()
    if name.isnumeric():
        raise ValueError('Wrong name.')
    information = ' '.join(normalize_data.split(' ')[1:])
    if 10 <= len(information) <= 13 and information[1:].isdigit():
        information = phone_validator(information)
    return name, information
