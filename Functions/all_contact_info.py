def all_contact_info(name: str, book):
    name = name.strip().title()
    if name not in book.data.keys():
        return f'Contact with the name [{name}] not found.'
    contact = book[name]
    contact_info = contact.get_all_info()
    result = ''
    for key in contact_info:
        if isinstance(contact_info[key], str):
            result += f'[{key}]: [{contact_info[key]}]\n'
        elif isinstance(contact_info[key], list):
            if key == 'phones':
                result += f'[{key}]: '
                for value in contact_info[key]:
                    result += f'[{value}], '
                result += '\b\b\n'
            elif key == 'notes':
                result += f'[{key}]:\n'
                for note in contact_info[key]:
                    result += f'[{note}]:\n'
            else:
                result += f'[{key}]: [{contact_info[key]}]\n'
    return result
