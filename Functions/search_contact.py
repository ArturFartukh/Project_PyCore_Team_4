from main import book
from phone_validator import *


def search_contact(data: str) -> str:

    name = None
    phone = None
    contact = None

    if data[0].isalpha():
        name = data.strip().lower()
    elif data[0].isdigit() or (data[0] == '+' and data[1:].isdigit()):
        phone = phone_validator(data)

    if name and name not in book.data.keys():
        return f'Contact with the name [{name}] not found.'
    elif name:
        contact = book[name]
    elif phone:
        for record in book.data:
            if record.phone_in_contact(phone):
                contact = record
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
