from support_funcs import phone_validator


def search_contact_func(data: str, book) -> str:

    name = None
    phone = None
    contact = None

    if data[0].isalpha():
        name = data.strip().title()
    elif data[0].isdigit() or (data[0] == '+' and data[1:].isdigit()):
        phone = phone_validator(data)

    if name and name not in book.data.keys():
        return f'Contact with the name [{name}] not found.'
    elif name:
        contact = book[name]
    elif phone:
        for key in book.data.keys():
            if book[key].has_phone(phone):
                contact = book[key]
    else:
        return 'Nothing found.\n'

    contact_info = contact.get_all_info()
    result = ''
    for key in contact_info:
        result += f'{key}: '
        if isinstance(contact_info[key], list):
            for item in contact_info[key]:
                result += f'{item}, '
            result += '\b\b'
        else:
            result += f'{contact_info[key]}'
        result += '\n'
    return result
