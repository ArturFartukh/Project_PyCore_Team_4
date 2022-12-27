from support_funcs import phone_validator


def split_data(data: str) -> tuple:
    normalize_data = data.strip()
    name = normalize_data.split(' ')[0].title()
    if name.isnumeric():
        return 'Wrong name.\n'
    information = ' '.join(normalize_data.split(' ')[1:])
    information = phone_validator(information)

    return name, information
