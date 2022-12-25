from main import book


def searsh_contact(data: str) -> str:
    name = data.strip().title()
    result = ''
    if name not in book.data.keys():
        return f'Contact with the name [{name}] not found.'
    contact = book[name]
    contact_info = contact.get_all_info()
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
