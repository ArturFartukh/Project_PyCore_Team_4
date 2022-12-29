from dzvina_assist.support_funcs import phone_validator


def split_data(data: str) -> tuple:
    if not data:
        name = ''
        information = ''
        return name, information
    normalize_data = data.strip()
    name = normalize_data.split(' ')[0].strip().title()
    if not name[0].isalpha():
        name = ''
    information = ' '.join(normalize_data.split(' ')[1:])
    if 10 <= len(information) <= 13 and information[1:].isdigit():
        information = phone_validator(information)

    return name, information
