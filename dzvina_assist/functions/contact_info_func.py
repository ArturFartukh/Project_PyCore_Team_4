def contact_info_func(name: str, book):
    name = name.strip().title()
    if name not in book.data:
        return f'<<< Contact with the name [{name}] not found.'
    contact = book[name]
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
            result += f'{key.title()}: {contact_info[key]})\n'
    return result