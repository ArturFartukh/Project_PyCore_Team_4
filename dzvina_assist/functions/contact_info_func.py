from dzvina_assist.support_funcs import phone_validator


def contact_info_func(book):
    name = None
    phone = None
    contact = None

    data = input('Please enter name or phone: ')
    data = data.strip()
    if data[0].isalpha():
        name = data.title()
    elif data[0].isdigit() or (data[0] == '+' and data[1:].isdigit()):
        phone = phone_validator(data)

    if name and name not in book.data:
        return f'<<< Contact with the name [{name}] not found.'
    elif name:
        contact = book[name]
    elif phone:
        for key in book.data:
            if book[key].has_phone(phone):
                contact = book[key]
    else:
        return '<<< Nothing found.\n'
    contact_info = contact.get_all_info()
    result = ''
    for key in contact_info:
        if isinstance(contact_info[key], str):
            result += f'{key.title()}: {contact_info[key]}\n'
        elif isinstance(contact_info[key], list):
            if key == 'phones':
                result += f'{key.title()}: '
                for count, value in enumerate(contact_info[key], 1):
                    if count in (4, 7, 10):
                        result += f'\n{" " * 8}'
                    result += f'{value}, '
                result += '\b\b\n'
            elif key == 'notes':
                result += f'{"-" * 30}\n'
                result += f'[{key.title()}]:\n'
                for count, note in enumerate(contact_info[key], 1):
                    result += f'{count}. [{note}]\n'
        else:
            result += f'{key.title()}: {contact_info[key]} (after: {contact.next_birthday()})\n'
    return result


def all_contact_info_func(book):
    result = ''
    if not book.data:
        return f'<<< The address book has no contacts yet.'
    for i, kay in enumerate(book.data, 1):
        contact = book[kay]
        contact_info = contact.get_all_info()
        result += f'\n{" " * 10}{i} contact\n'
        for key in contact_info:
            if isinstance(contact_info[key], str):
                result += f'{key.title()}: {contact_info[key]}\n'
            elif isinstance(contact_info[key], list):
                if key == 'phones':
                    result += f'{key.title()}: '
                    for count, value in enumerate(contact_info[key], 1):
                        if count in (4, 7, 10, 13, 16):
                            result += f'\n{" " * 8}'
                        result += f'{value}, '
                    result += '\b\b\n'
                elif key == 'notes':
                    result += f'{"-" * 30}\n'
                    result += f'[{key.title()}]:\n'
                    for count, note in enumerate(contact_info[key], 1):
                        result += f'{count}. [{note}]\n'
            else:
                result += f'{key.title()}: {contact_info[key]} (after: {contact.next_birthday()})\n'
        result += f'{"=" * 38}\n'
    return result
